from src.dofus_object import DofusObject, Caracteristique

bottines_mulou = {
    "id":
    1032,
    "official":
    6953,
    "picture":
    11076,
    "level":
    61,
    "cloth_id":
    32,
    "choose_effect":
    0,
    "give_boost":
    0,
    "cannot_fm":
    0,
    "category_id":
    19,
    "subcategory_id":
    None,
    "name":
    "Bottines du Mulou",
    "information":
    None,
    "category_name":
    "bo",
    "category_type":
    "E",
    "subcategory_name":
    None,
    "cloth_name":
    "Panoplie du Mulou",
    "description":
    "Ces bottines recouvertes de poils de Mulou, sont très pratiques pour nettoyer les parquets poussiéreux, ou tout simplement pour nettoyer la tête de vos adversaires lorsqu'ils sont au sol en train d'agoniser.",
    "swf":
    None,
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
    None,
    "slug":
    "1032-bottines-du-mulou",
    "effects": [{
        "item_id": 1032,
        "id": 130,
        "name": "vi",
        "type": "E",
        "min": 21,
        "max": 25,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 1032,
        "id": 170,
        "name": "ag",
        "type": "E",
        "min": 16,
        "max": 20,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 1032,
        "id": 220,
        "name": "pm",
        "type": "E",
        "min": 1,
        "max": 1,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }, {
        "item_id": 1032,
        "id": 480,
        "name": "rtp",
        "type": "E",
        "min": 2,
        "max": 2,
        "emote": None,
        "title": None,
        "spell": None,
        "spellDesc": None
    }],
    "constraints": [],
    "ingredients": [{
        "item_id": 1032,
        "id": 748,
        "name": "Magnésite",
        "picture": 40659,
        "count": 2
    }, {
        "item_id": 1032,
        "id": 2482,
        "name": "Charnière Cassée",
        "picture": 15942,
        "count": 7
    }, {
        "item_id": 1032,
        "id": 2506,
        "name": "Grelot",
        "picture": 15529,
        "count": 1
    }, {
        "item_id": 1032,
        "id": 9384,
        "name": "Fleur de Blop Griotte Royal",
        "picture": 35012,
        "count": 1
    }, {
        "item_id": 1032,
        "id": 13715,
        "name": "Dent de Larve Dorée",
        "picture": 47803,
        "count": 2
    }],
    "weapon":
    None
}


def test_object_creation():
    bottines = DofusObject(bottines_mulou)
    assert bottines.name == "Bottines du Mulou"
    assert bottines.level == 61
    assert str(bottines.effects[0]) == "{'name': 'vi', 'min': 21, 'max': 25}"
    assert str(bottines.ingredients[0]
               ) == "{'name': 'Magnésite', 'count': 2, 'prix': 1000000000}"
    assert bottines.cout_fabrication() == 5000000000
    assert bottines.nombre_ingredients == 5
    assert bottines.gain_estime() == 0.0
    # assert gain_brisage(5190) == 28260
