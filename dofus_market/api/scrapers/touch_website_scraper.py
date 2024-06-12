from market.database.metier import Metier
import json
import requests
from bs4 import BeautifulSoup
import re
import json
import requests
import asyncio
import aiohttp
import itertools

default_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0' }
touch_domain = "https://www.dofus-touch.com"

async def query_page(session, page, headers=default_headers):
    async with session.get(page, headers=headers) as response:
        return await response.text()
    
async def query_all_pages(pages, headers=default_headers):
    queries = []
    async with aiohttp.ClientSession() as session:
        queries = await asyncio.gather(*[TouchWebsiteScraper.query_page(session, page, headers) for page in pages], return_exceptions=True)
    return [q for q in queries]

class TouchWebsiteScraper:
    professions = {}
    recipes = []
    missing_pages = []

    async def generate_professions(self):
        self.professions = {}
        profession_pages = await query_all_pages(f'https://www.dofus-touch.com/fr/mmorpg/encyclopedie/metiers?display=table&page={i+1}' for i in [0, 1])
        for profession_page in profession_pages[0:1]:
            soup = BeautifulSoup(profession_page, 'html.parser')

            # The page is composed of a list of professions. First get the panel where they are located
            main_panel = soup.find("div", "ak-container ak-main-center")

            # The look for each item
            profession_items = main_panel.find_all("td", "item-name")
            assert(len(profession_items) > 0)

            for profession_item in profession_items:
                # The profession item is composed of the "item-name" containing the name in the string and a child "a" link
                self.professions[profession_item.string.strip()] = {"link":profession_item.find("a", href=re.compile("encyclopedie/metiers/")).get("href")}

    async def generate_recipes(self):
        if (not self.professions):
            self.generate_professions()

        profession_pages = await query_all_pages([l for l in [touch_domain + l["link"] + "/recipes" for l in self.professions.values()]])
        self.recipes = []
        for [[profession_name, profession], profession_first_page] in zip(self.professions.items(), profession_pages): 
            page_id = 1
            page = profession_first_page
            profession["recipes"] = []
            while (page != None):
                profession_page = BeautifulSoup(page, 'html.parser')

                # There should be a tab content panel containing tabs for harvests and recipes
                tab_panel = profession_page.find("div", "tab-content") 

                # Get the currently active tab, which should be the recipes. Inactive tabs will have the "ak-tab hide" class
                recipe_tabs = [f for f in tab_panel.find_all("div", "ak-tab") if "hide" not in f["class"]]
                
                # We only expect magus items to be without a tab
                if (len(recipe_tabs) == 0):
                    assert("mage" in profession_name)
                    page = None
                    continue

                # Go the the tab body
                tab_body = recipe_tabs[0].find("tbody")

                # This body should have a list of "tr" elements with the recipe dynamically loadable
                recipes_tr = tab_body.find_all("tr", attrs={"ajax-details-url":re.compile("objets/recette/")})
                
                for recipe_tr in recipes_tr:
                    recipe = {}

                    # The recipe contains a link to the crafted resource
                    link_html  = recipe_tr.find("a", href=re.compile("encyclopedie/"))

                    # Row contains the name of the object, then the level. link_html is the child of the name container, which is sibling of the level's container
                    level_html = link_html.parent.findNextSibling("td")

                    # The detail url is of form "/en/mmorpg/encyclopedia/items/recipe/286", 286 being the item id
                    recipe["detail_url"]    = recipe_tr.get("ajax-details-url")
                    recipe["object_id"]     = int(recipe["detail_url"].split("/")[-1])
                    recipe["object_name"]   = link_html.string
                    recipe["link"]          = link_html.get("href")
                    recipe["level"]         = int(level_html.string)
                    recipe["profession"]    = profession_name

                    self.recipes.append(recipe)
                    profession["recipes"].append(recipe)

                page_id += 1
                page = None
                next_page_link = profession_page.find("link", rel="next", href=re.compile(profession["link"]))
                if next_page_link != None:
                    page = requests.get(touch_domain + next_page_link.get("href"), headers=default_headers).text

    async def generate_recipe_ingredients(self):
        if (not recipes):
            self.generate_recipes()

        request_count = 0
        self.missing_pages = []
        for [name, profession] in self.professions.items():
            
            print(name)
            recipes = profession["recipes"]
            recipe_fetch_headers = {
                "Accept"        :"*/*",
                "X-Requested-With": "XMLHttpRequest",
                "Referer"       :profession["link"] + "/recipes",
                "Sec-Fetch-Dest":"empty",
                "Sec-Fetch-Mode":"cors",
                "Sec-Fetch-Site":"same-origin",
                "User-Agent"    :"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
            }

            request_count += len(recipes) 
            all_recipe_json = await query_all_pages([f"https://www.dofus-touch.com/fr/mmorpg/encyclopedie/objets/recette/" + str(r["object_id"]) for r in recipes], headers=recipe_fetch_headers)
            all_recipe_html = [json.loads(j) for j in all_recipe_json]

            recipe["ingredients"] = []

            for [recipe, html] in zip(recipes, all_recipe_html):
                # For some reason some recepy html are empty. Should probably tell ankama...
                if html == "":
                    continue

                soup = BeautifulSoup(html, "html.parser")

                # We also have 404 errors on some object links. Ankama fix link plz
                if (soup.find("div", "ak-404")):
                    self.missing_pages.append([recipe, soup])
                    continue

                # This documennt is a grid of objects. First find the container of the grid
                grid_container = soup.find("div", "ak-content-list")

                # Now we can get all the items in the grid. They are all of the "ak-list-element" class
                items = grid_container.find_all("div", "ak-list-element")

                ingredients = []

                for item in items:
                    # The item count is embedded in a text in front of the content : e.g "10 x" contained in a "ak-front" element
                    item_count_text = item.find("div", "ak-front")
                    item_count = re.match("(\d+) x", item_count_text.string.strip()).group(1)
                    
                    # Now go and get the item properties, they are all in a div under the item
                    content = item.find("div", "ak-content")

                    ingredient = {}

                    # Gather the data.
                    ingredient["count"] = item_count
                    ingredient["link"] = content.find("a").get("href")
                    ingredient["name"] = content.find("span", "ak-linker").string
                    ingredients.append(ingredient)

                recipe["ingredients"] = ingredients
                
            # Force a wait to avoid being blocked out of the website. Limit rate of cloudfront is 5 minutes, so we assume we need to wait that much
            # 500 is arbitrary, we can probably spam our way to a precise number but that should do for now
            if (request_count > 500):
                request_count = 0
                await asyncio.sleep(5 * 60 + 1)

    def populate_professions_db(self):
        Metier.objects.bulk_create([Metier(name=name) for name in self.professions.keys()])

    def populate_recipes_db(self):
        #todo