# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_market.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11grpc_market.proto\x12\x18\x64ofus_market.grpc_market\x1a\x1bgoogle/protobuf/empty.proto"\x8c\x01\n\nBrokenRune\x12\x0c\n\x04rune\x18\x01 \x01(\t\x12\x13\n\x0bquantity_ra\x18\x02 \x01(\x02\x12\x0f\n\x07prix_ra\x18\x03 \x01(\x05\x12\x13\n\x0bquantity_pa\x18\x04 \x01(\x02\x12\x0f\n\x07prix_pa\x18\x05 \x01(\x05\x12\x13\n\x0bquantity_ba\x18\x06 \x01(\x02\x12\x0f\n\x07prix_ba\x18\x07 \x01(\x05"G\n\x04Rune\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07prix_ra\x18\x02 \x01(\x05\x12\x0f\n\x07prix_pa\x18\x03 \x01(\x05\x12\x0f\n\x07prix_ba\x18\x04 \x01(\x05"g\n\x0f\x43\x61racteristique\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0b\n\x03max\x18\x03 \x01(\x05\x12,\n\x04rune\x18\x04 \x01(\x0b\x32\x1e.dofus_market.grpc_market.Rune"\xf8\x01\n\nIngredient\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\r\n\x05price\x18\x03 \x01(\x05\x12\x39\n\x0bingredients\x18\x04 \x03(\x0b\x32$.dofus_market.grpc_market.Ingredient\x12\x15\n\x08nb_objet\x18\x05 \x01(\x05H\x00\x88\x01\x01\x12\x1d\n\x10\x63out_fabrication\x18\x06 \x01(\x02H\x01\x88\x01\x01\x12\x18\n\x0brentabilite\x18\x07 \x01(\x02H\x02\x88\x01\x01\x42\x0b\n\t_nb_objetB\x13\n\x11_cout_fabricationB\x0e\n\x0c_rentabilite"(\n\x18\x45quipementDetailsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\xcc\x02\n\x19\x45quipementDetailsResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x18\n\x10\x63out_fabrication\x18\x03 \x01(\x02\x12\x13\n\x0bgain_estime\x18\x04 \x01(\x02\x12\x13\n\x0brentabilite\x18\x05 \x01(\x02\x12\x10\n\x08nb_objet\x18\x06 \x01(\x05\x12\x0e\n\x06metier\x18\x07 \x01(\t\x12:\n\x07\x65\x66\x66\x65\x63ts\x18\x08 \x03(\x0b\x32).dofus_market.grpc_market.Caracteristique\x12\x39\n\x0bingredients\x18\t \x03(\x0b\x32$.dofus_market.grpc_market.Ingredient\x12\x35\n\x07\x62risage\x18\n \x03(\x0b\x32$.dofus_market.grpc_market.BrokenRune"\x17\n\x15\x45quipementListRequest"f\n\x16\x45quipementListResponse\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.dofus_market.grpc_market.EquipementResponse\x12\r\n\x05\x63ount\x18\x02 \x01(\x05"\x97\x01\n\x12\x45quipementResponse\x12\x0e\n\x06metier\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\r\n\x05level\x18\t \x01(\x05\x12\x18\n\x10\x63out_fabrication\x18\n \x01(\x02\x12\x13\n\x0bgain_estime\x18\x0b \x01(\x02\x12\x13\n\x0brentabilite\x18\x0c \x01(\x02\x12\x10\n\x08nb_objet\x18\r \x01(\x05")\n\x19\x45quipementRetrieveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"(\n\x18IngredientDestroyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t".\n IngredientForCraftDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05"\x1f\n\x1dIngredientForCraftListRequest"g\n\x1eIngredientForCraftListResponse\x12\x45\n\x07results\x18\x01 \x03(\x0b\x32\x34.dofus_market.grpc_market.IngredientForCraftResponse"\x86\x01\n&IngredientForCraftPartialUpdateRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x12\n\ningredient\x18\x04 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x05 \x03(\tB\x05\n\x03_id"Y\n\x19IngredientForCraftRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x12\n\ningredient\x18\x03 \x01(\tB\x05\n\x03_id"Z\n\x1aIngredientForCraftResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x12\n\ningredient\x18\x03 \x01(\tB\x05\n\x03_id"/\n!IngredientForCraftRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05"\x17\n\x15IngredientListRequest"W\n\x16IngredientListResponse\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.dofus_market.grpc_market.IngredientResponse"l\n\x1eIngredientPartialUpdateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05price\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x04 \x03(\tB\x08\n\x06_price"?\n\x11IngredientRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05price\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_price"@\n\x12IngredientResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05price\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_price")\n\x19IngredientRetrieveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"$\n\x14MetierDestroyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x13\n\x11MetierListRequest"O\n\x12MetierListResponse\x12\x39\n\x07results\x18\x01 \x03(\x0b\x32(.dofus_market.grpc_market.MetierResponse"J\n\x1aMetierPartialUpdateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x02 \x03(\t"\x1d\n\rMetierRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x1e\n\x0eMetierResponse\x12\x0c\n\x04name\x18\x01 \x01(\t"%\n\x15MetierRetrieveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"+\n\x15RecetteDestroyRequest\x12\x12\n\ningredient\x18\x01 \x01(\t"\x14\n\x12RecetteListRequest"Q\n\x13RecetteListResponse\x12:\n\x07results\x18\x01 \x03(\x0b\x32).dofus_market.grpc_market.RecetteResponse"\xa4\x01\n\x1bRecettePartialUpdateRequest\x12\x12\n\ningredient\x18\x01 \x01(\t\x12\x12\n\x05level\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06metier\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bingredients\x18\x05 \x03(\x03\x12\x1e\n\x16_partial_update_fields\x18\x06 \x03(\tB\x08\n\x06_levelB\t\n\x07_metier"w\n\x0eRecetteRequest\x12\x12\n\ningredient\x18\x01 \x01(\t\x12\x12\n\x05level\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06metier\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bingredients\x18\x04 \x03(\x03\x42\x08\n\x06_levelB\t\n\x07_metier"x\n\x0fRecetteResponse\x12\x12\n\ningredient\x18\x01 \x01(\t\x12\x12\n\x05level\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06metier\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bingredients\x18\x04 \x03(\x03\x42\x08\n\x06_levelB\t\n\x07_metier",\n\x16RecetteRetrieveRequest\x12\x12\n\ningredient\x18\x01 \x01(\t""\n\x12RuneDestroyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x11\n\x0fRuneListRequest"K\n\x10RuneListResponse\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.dofus_market.grpc_market.RuneResponse"\xae\x01\n\x18RunePartialUpdateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x07prix_ra\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07prix_pa\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07prix_ba\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x1e\n\x16_partial_update_fields\x18\x06 \x03(\tB\n\n\x08_prix_raB\n\n\x08_prix_paB\n\n\x08_prix_ba"\x81\x01\n\x0bRuneRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x07prix_ra\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07prix_pa\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07prix_ba\x18\x04 \x01(\x05H\x02\x88\x01\x01\x42\n\n\x08_prix_raB\n\n\x08_prix_paB\n\n\x08_prix_ba"\x82\x01\n\x0cRuneResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x07prix_ra\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07prix_pa\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07prix_ba\x18\x04 \x01(\x05H\x02\x88\x01\x01\x42\n\n\x08_prix_raB\n\n\x08_prix_paB\n\n\x08_prix_ba"#\n\x13RuneRetrieveRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xea\x02\n\x14\x45quipementController\x12t\n\x07\x44\x65tails\x12\x32.dofus_market.grpc_market.EquipementDetailsRequest\x1a\x33.dofus_market.grpc_market.EquipementDetailsResponse"\x00\x12k\n\x04List\x12/.dofus_market.grpc_market.EquipementListRequest\x1a\x30.dofus_market.grpc_market.EquipementListResponse"\x00\x12o\n\x08Retrieve\x12\x33.dofus_market.grpc_market.EquipementRetrieveRequest\x1a,.dofus_market.grpc_market.EquipementResponse"\x00\x32\x96\x05\n\x14IngredientController\x12\x65\n\x06\x43reate\x12+.dofus_market.grpc_market.IngredientRequest\x1a,.dofus_market.grpc_market.IngredientResponse"\x00\x12W\n\x07\x44\x65stroy\x12\x32.dofus_market.grpc_market.IngredientDestroyRequest\x1a\x16.google.protobuf.Empty"\x00\x12k\n\x04List\x12/.dofus_market.grpc_market.IngredientListRequest\x1a\x30.dofus_market.grpc_market.IngredientListResponse"\x00\x12y\n\rPartialUpdate\x12\x38.dofus_market.grpc_market.IngredientPartialUpdateRequest\x1a,.dofus_market.grpc_market.IngredientResponse"\x00\x12o\n\x08Retrieve\x12\x33.dofus_market.grpc_market.IngredientRetrieveRequest\x1a,.dofus_market.grpc_market.IngredientResponse"\x00\x12\x65\n\x06Update\x12+.dofus_market.grpc_market.IngredientRequest\x1a,.dofus_market.grpc_market.IngredientResponse"\x00\x32\xf7\x05\n\x1cIngredientForCraftController\x12u\n\x06\x43reate\x12\x33.dofus_market.grpc_market.IngredientForCraftRequest\x1a\x34.dofus_market.grpc_market.IngredientForCraftResponse"\x00\x12_\n\x07\x44\x65stroy\x12:.dofus_market.grpc_market.IngredientForCraftDestroyRequest\x1a\x16.google.protobuf.Empty"\x00\x12{\n\x04List\x12\x37.dofus_market.grpc_market.IngredientForCraftListRequest\x1a\x38.dofus_market.grpc_market.IngredientForCraftListResponse"\x00\x12\x89\x01\n\rPartialUpdate\x12@.dofus_market.grpc_market.IngredientForCraftPartialUpdateRequest\x1a\x34.dofus_market.grpc_market.IngredientForCraftResponse"\x00\x12\x7f\n\x08Retrieve\x12;.dofus_market.grpc_market.IngredientForCraftRetrieveRequest\x1a\x34.dofus_market.grpc_market.IngredientForCraftResponse"\x00\x12u\n\x06Update\x12\x33.dofus_market.grpc_market.IngredientForCraftRequest\x1a\x34.dofus_market.grpc_market.IngredientForCraftResponse"\x00\x32\xe6\x04\n\x10MetierController\x12]\n\x06\x43reate\x12\'.dofus_market.grpc_market.MetierRequest\x1a(.dofus_market.grpc_market.MetierResponse"\x00\x12S\n\x07\x44\x65stroy\x12..dofus_market.grpc_market.MetierDestroyRequest\x1a\x16.google.protobuf.Empty"\x00\x12\x63\n\x04List\x12+.dofus_market.grpc_market.MetierListRequest\x1a,.dofus_market.grpc_market.MetierListResponse"\x00\x12q\n\rPartialUpdate\x12\x34.dofus_market.grpc_market.MetierPartialUpdateRequest\x1a(.dofus_market.grpc_market.MetierResponse"\x00\x12g\n\x08Retrieve\x12/.dofus_market.grpc_market.MetierRetrieveRequest\x1a(.dofus_market.grpc_market.MetierResponse"\x00\x12]\n\x06Update\x12\'.dofus_market.grpc_market.MetierRequest\x1a(.dofus_market.grpc_market.MetierResponse"\x00\x32\xf2\x04\n\x11RecetteController\x12_\n\x06\x43reate\x12(.dofus_market.grpc_market.RecetteRequest\x1a).dofus_market.grpc_market.RecetteResponse"\x00\x12T\n\x07\x44\x65stroy\x12/.dofus_market.grpc_market.RecetteDestroyRequest\x1a\x16.google.protobuf.Empty"\x00\x12\x65\n\x04List\x12,.dofus_market.grpc_market.RecetteListRequest\x1a-.dofus_market.grpc_market.RecetteListResponse"\x00\x12s\n\rPartialUpdate\x12\x35.dofus_market.grpc_market.RecettePartialUpdateRequest\x1a).dofus_market.grpc_market.RecetteResponse"\x00\x12i\n\x08Retrieve\x12\x30.dofus_market.grpc_market.RecetteRetrieveRequest\x1a).dofus_market.grpc_market.RecetteResponse"\x00\x12_\n\x06Update\x12(.dofus_market.grpc_market.RecetteRequest\x1a).dofus_market.grpc_market.RecetteResponse"\x00\x32\xce\x04\n\x0eRuneController\x12Y\n\x06\x43reate\x12%.dofus_market.grpc_market.RuneRequest\x1a&.dofus_market.grpc_market.RuneResponse"\x00\x12Q\n\x07\x44\x65stroy\x12,.dofus_market.grpc_market.RuneDestroyRequest\x1a\x16.google.protobuf.Empty"\x00\x12_\n\x04List\x12).dofus_market.grpc_market.RuneListRequest\x1a*.dofus_market.grpc_market.RuneListResponse"\x00\x12m\n\rPartialUpdate\x12\x32.dofus_market.grpc_market.RunePartialUpdateRequest\x1a&.dofus_market.grpc_market.RuneResponse"\x00\x12\x63\n\x08Retrieve\x12-.dofus_market.grpc_market.RuneRetrieveRequest\x1a&.dofus_market.grpc_market.RuneResponse"\x00\x12Y\n\x06Update\x12%.dofus_market.grpc_market.RuneRequest\x1a&.dofus_market.grpc_market.RuneResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "grpc_market_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_BROKENRUNE"]._serialized_start = 77
    _globals["_BROKENRUNE"]._serialized_end = 217
    _globals["_RUNE"]._serialized_start = 219
    _globals["_RUNE"]._serialized_end = 290
    _globals["_CARACTERISTIQUE"]._serialized_start = 292
    _globals["_CARACTERISTIQUE"]._serialized_end = 395
    _globals["_INGREDIENT"]._serialized_start = 398
    _globals["_INGREDIENT"]._serialized_end = 646
    _globals["_EQUIPEMENTDETAILSREQUEST"]._serialized_start = 648
    _globals["_EQUIPEMENTDETAILSREQUEST"]._serialized_end = 688
    _globals["_EQUIPEMENTDETAILSRESPONSE"]._serialized_start = 691
    _globals["_EQUIPEMENTDETAILSRESPONSE"]._serialized_end = 1023
    _globals["_EQUIPEMENTLISTREQUEST"]._serialized_start = 1025
    _globals["_EQUIPEMENTLISTREQUEST"]._serialized_end = 1048
    _globals["_EQUIPEMENTLISTRESPONSE"]._serialized_start = 1050
    _globals["_EQUIPEMENTLISTRESPONSE"]._serialized_end = 1152
    _globals["_EQUIPEMENTRESPONSE"]._serialized_start = 1155
    _globals["_EQUIPEMENTRESPONSE"]._serialized_end = 1306
    _globals["_EQUIPEMENTRETRIEVEREQUEST"]._serialized_start = 1308
    _globals["_EQUIPEMENTRETRIEVEREQUEST"]._serialized_end = 1349
    _globals["_INGREDIENTDESTROYREQUEST"]._serialized_start = 1351
    _globals["_INGREDIENTDESTROYREQUEST"]._serialized_end = 1391
    _globals["_INGREDIENTFORCRAFTDESTROYREQUEST"]._serialized_start = 1393
    _globals["_INGREDIENTFORCRAFTDESTROYREQUEST"]._serialized_end = 1439
    _globals["_INGREDIENTFORCRAFTLISTREQUEST"]._serialized_start = 1441
    _globals["_INGREDIENTFORCRAFTLISTREQUEST"]._serialized_end = 1472
    _globals["_INGREDIENTFORCRAFTLISTRESPONSE"]._serialized_start = 1474
    _globals["_INGREDIENTFORCRAFTLISTRESPONSE"]._serialized_end = 1577
    _globals["_INGREDIENTFORCRAFTPARTIALUPDATEREQUEST"]._serialized_start = 1580
    _globals["_INGREDIENTFORCRAFTPARTIALUPDATEREQUEST"]._serialized_end = 1714
    _globals["_INGREDIENTFORCRAFTREQUEST"]._serialized_start = 1716
    _globals["_INGREDIENTFORCRAFTREQUEST"]._serialized_end = 1805
    _globals["_INGREDIENTFORCRAFTRESPONSE"]._serialized_start = 1807
    _globals["_INGREDIENTFORCRAFTRESPONSE"]._serialized_end = 1897
    _globals["_INGREDIENTFORCRAFTRETRIEVEREQUEST"]._serialized_start = 1899
    _globals["_INGREDIENTFORCRAFTRETRIEVEREQUEST"]._serialized_end = 1946
    _globals["_INGREDIENTLISTREQUEST"]._serialized_start = 1948
    _globals["_INGREDIENTLISTREQUEST"]._serialized_end = 1971
    _globals["_INGREDIENTLISTRESPONSE"]._serialized_start = 1973
    _globals["_INGREDIENTLISTRESPONSE"]._serialized_end = 2060
    _globals["_INGREDIENTPARTIALUPDATEREQUEST"]._serialized_start = 2062
    _globals["_INGREDIENTPARTIALUPDATEREQUEST"]._serialized_end = 2170
    _globals["_INGREDIENTREQUEST"]._serialized_start = 2172
    _globals["_INGREDIENTREQUEST"]._serialized_end = 2235
    _globals["_INGREDIENTRESPONSE"]._serialized_start = 2237
    _globals["_INGREDIENTRESPONSE"]._serialized_end = 2301
    _globals["_INGREDIENTRETRIEVEREQUEST"]._serialized_start = 2303
    _globals["_INGREDIENTRETRIEVEREQUEST"]._serialized_end = 2344
    _globals["_METIERDESTROYREQUEST"]._serialized_start = 2346
    _globals["_METIERDESTROYREQUEST"]._serialized_end = 2382
    _globals["_METIERLISTREQUEST"]._serialized_start = 2384
    _globals["_METIERLISTREQUEST"]._serialized_end = 2403
    _globals["_METIERLISTRESPONSE"]._serialized_start = 2405
    _globals["_METIERLISTRESPONSE"]._serialized_end = 2484
    _globals["_METIERPARTIALUPDATEREQUEST"]._serialized_start = 2486
    _globals["_METIERPARTIALUPDATEREQUEST"]._serialized_end = 2560
    _globals["_METIERREQUEST"]._serialized_start = 2562
    _globals["_METIERREQUEST"]._serialized_end = 2591
    _globals["_METIERRESPONSE"]._serialized_start = 2593
    _globals["_METIERRESPONSE"]._serialized_end = 2623
    _globals["_METIERRETRIEVEREQUEST"]._serialized_start = 2625
    _globals["_METIERRETRIEVEREQUEST"]._serialized_end = 2662
    _globals["_RECETTEDESTROYREQUEST"]._serialized_start = 2664
    _globals["_RECETTEDESTROYREQUEST"]._serialized_end = 2707
    _globals["_RECETTELISTREQUEST"]._serialized_start = 2709
    _globals["_RECETTELISTREQUEST"]._serialized_end = 2729
    _globals["_RECETTELISTRESPONSE"]._serialized_start = 2731
    _globals["_RECETTELISTRESPONSE"]._serialized_end = 2812
    _globals["_RECETTEPARTIALUPDATEREQUEST"]._serialized_start = 2815
    _globals["_RECETTEPARTIALUPDATEREQUEST"]._serialized_end = 2979
    _globals["_RECETTEREQUEST"]._serialized_start = 2981
    _globals["_RECETTEREQUEST"]._serialized_end = 3100
    _globals["_RECETTERESPONSE"]._serialized_start = 3102
    _globals["_RECETTERESPONSE"]._serialized_end = 3222
    _globals["_RECETTERETRIEVEREQUEST"]._serialized_start = 3224
    _globals["_RECETTERETRIEVEREQUEST"]._serialized_end = 3268
    _globals["_RUNEDESTROYREQUEST"]._serialized_start = 3270
    _globals["_RUNEDESTROYREQUEST"]._serialized_end = 3304
    _globals["_RUNELISTREQUEST"]._serialized_start = 3306
    _globals["_RUNELISTREQUEST"]._serialized_end = 3323
    _globals["_RUNELISTRESPONSE"]._serialized_start = 3325
    _globals["_RUNELISTRESPONSE"]._serialized_end = 3400
    _globals["_RUNEPARTIALUPDATEREQUEST"]._serialized_start = 3403
    _globals["_RUNEPARTIALUPDATEREQUEST"]._serialized_end = 3577
    _globals["_RUNEREQUEST"]._serialized_start = 3580
    _globals["_RUNEREQUEST"]._serialized_end = 3709
    _globals["_RUNERESPONSE"]._serialized_start = 3712
    _globals["_RUNERESPONSE"]._serialized_end = 3842
    _globals["_RUNERETRIEVEREQUEST"]._serialized_start = 3844
    _globals["_RUNERETRIEVEREQUEST"]._serialized_end = 3879
    _globals["_EQUIPEMENTCONTROLLER"]._serialized_start = 3882
    _globals["_EQUIPEMENTCONTROLLER"]._serialized_end = 4244
    _globals["_INGREDIENTCONTROLLER"]._serialized_start = 4247
    _globals["_INGREDIENTCONTROLLER"]._serialized_end = 4909
    _globals["_INGREDIENTFORCRAFTCONTROLLER"]._serialized_start = 4912
    _globals["_INGREDIENTFORCRAFTCONTROLLER"]._serialized_end = 5671
    _globals["_METIERCONTROLLER"]._serialized_start = 5674
    _globals["_METIERCONTROLLER"]._serialized_end = 6288
    _globals["_RECETTECONTROLLER"]._serialized_start = 6291
    _globals["_RECETTECONTROLLER"]._serialized_end = 6917
    _globals["_RUNECONTROLLER"]._serialized_start = 6920
    _globals["_RUNECONTROLLER"]._serialized_end = 7510
# @@protoc_insertion_point(module_scope)