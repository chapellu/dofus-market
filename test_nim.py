from src.dofus_object import DofusObject

pelle_houze = DofusObject({
    "id":
    2475,
    "official":
    1432,
    "picture":
    8017,
    "level":
    24,
    "cloth_id":
    None,
    "choose_effect":
    0,
    "give_boost":
    0,
    "cannot_fm":
    0,
    "category_id":
    9,
    "subcategory_id":
    None,
    "name":
    "Pelle Houze",
    "information":
    None,
    "category_name":
    "pe",
    "category_type":
    "W",
    "subcategory_name":
    None,
    "cloth_name":
    None,
    "description":
    "Gaston Houze, jardinier disciple d'Enutrof, avait tendance à toujours trop abuser des plantes. Cette arme en est la preuve : puissante, elle aura tendance à vous jouer des tours et à mettre à mal votre intelligence.",
    "pa_cost":
    4,
    "po_min":
    1,
    "po_max":
    0,
    "cc_bonus":
    20,
    "cc_hits":
    10,
    "hits_count":
    1,
    "hits_lines":
    1,
    "one_hand":
    None,
    "incarnation":
    None,
    "etheral":
    None,
    "swf":
    766,
    "harness":
    None,
    "main_color1":
    None,
    "main_color2":
    None,
    "main_color3":
    None,
    "png_color1":
    None,
    "png_color2":
    None,
    "png_color3":
    None,
    "size":
    None,
    "cameleon":
    0,
    "slug":
    "2475-pelle-houze",
    "effects": [{
        "item_id": 2475,
        "id": 20,
        "name": "dt",
        "type": "D",
        "min": 11,
        "max": 16,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 2475,
        "id": 150,
        "name": "in",
        "type": "E",
        "min": -30,
        "max": -30,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 2475,
        "id": 140,
        "name": "fo",
        "type": "E",
        "min": 21,
        "max": 30,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 2475,
        "id": 130,
        "name": "vi",
        "type": "E",
        "min": -40,
        "max": -40,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 2475,
        "id": 310,
        "name": "so",
        "type": "E",
        "min": -15,
        "max": -15,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 2475,
        "id": 230,
        "name": "po",
        "type": "E",
        "min": 1,
        "max": 1,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }],
    "constraints": [],
    "ingredients": [{
        "item_id": 2475,
        "id": 442,
        "name": "Bronze",
        "picture": 39109,
        "count": 8
    }, {
        "item_id": 2475,
        "id": 444,
        "name": "Etain",
        "picture": 39078,
        "count": 8
    }, {
        "item_id": 2475,
        "id": 535,
        "name": "Farine de Houblon",
        "picture": 52253,
        "count": 6
    }],
    "weapon": {
        "pa_cost": 4,
        "po_min": 1,
        "po_max": 0,
        "cc_bonus": 20,
        "cc_hits": 10,
        "cc_rate": 0,
        "hits_count": 1,
        "hits_lines": 1,
        "one_hand": None,
        "incarnation": None,
        "etheral": None
    },
    "cc_rate":
    0
})

print(pelle_houze.effects)
print(pelle_houze.ingredients)
print(pelle_houze.nombre_ingredients)
pelle_houze.ingredients[0].prix = 12
pelle_houze.ingredients[1].prix = 10
pelle_houze.ingredients[2].prix = 4

print(pelle_houze.cout_fabrication())

print(pelle_houze.gain_estime())

print(pelle_houze.rentabilite())
