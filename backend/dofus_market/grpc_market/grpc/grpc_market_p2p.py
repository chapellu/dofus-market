# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.27.2
# Pydantic Version: 2.8.2
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class BrokenRune(BaseModel):
    rune: str = Field(default="")
    quantity_ra: float = Field(default=0.0)
    prix_ra: int = Field(default=0)
    quantity_pa: float = Field(default=0.0)
    prix_pa: int = Field(default=0)
    quantity_ba: float = Field(default=0.0)
    prix_ba: int = Field(default=0)


class Rune(BaseModel):
    name: str = Field(default="")
    prix_ra: int = Field(default=0)
    prix_pa: int = Field(default=0)
    prix_ba: int = Field(default=0)


class Caracteristique(BaseModel):
    name: str = Field(default="")
    min: int = Field(default=0)
    max: int = Field(default=0)
    rune: Rune = Field()


class Ingredient(BaseModel):
    name: str = Field(default="")
    quantity: int = Field(default=0)
    price: int = Field(default=0)
    ingredients: typing.List["Ingredient"] = Field(default_factory=list)
    nb_objet: typing.Optional[int] = Field(default=0)
    cout_fabrication: typing.Optional[float] = Field(default=0.0)
    rentabilite: typing.Optional[float] = Field(default=0.0)


class EquipementDetailsRequest(BaseModel):
    name: str = Field(default="")


class EquipementDetailsResponse(BaseModel):
    name: str = Field(default="")
    level: int = Field(default=0)
    cout_fabrication: float = Field(default=0.0)
    gain_estime: float = Field(default=0.0)
    rentabilite: float = Field(default=0.0)
    nb_objet: int = Field(default=0)
    metier: str = Field(default="")
    effects: typing.List[Caracteristique] = Field(default_factory=list)
    ingredients: typing.List[Ingredient] = Field(default_factory=list)
    brisage: typing.List[BrokenRune] = Field(default_factory=list)


class EquipementListRequest(BaseModel):
    pass


class EquipementResponse(BaseModel):
    metier: str = Field(default="")
    name: str = Field(default="")
    level: int = Field(default=0)
    cout_fabrication: float = Field(default=0.0)
    gain_estime: float = Field(default=0.0)
    rentabilite: int = Field(default=0)
    nb_objet: int = Field(default=0)


class EquipementListResponse(BaseModel):
    results: typing.List[EquipementResponse] = Field(default_factory=list)
    count: int = Field(default=0)


class EquipementRetrieveRequest(BaseModel):
    name: str = Field(default="")


class IngredientDestroyRequest(BaseModel):
    name: str = Field(default="")


class IngredientForCraftDestroyRequest(BaseModel):
    id: int = Field(default=0)


class IngredientForCraftListRequest(BaseModel):
    pass


class IngredientForCraftResponse(BaseModel):
    id: typing.Optional[int] = Field(default=0)
    quantity: int = Field(default=0)
    ingredient: str = Field(default="")


class IngredientForCraftListResponse(BaseModel):
    results: typing.List[IngredientForCraftResponse] = Field(
        default_factory=list)


class IngredientForCraftPartialUpdateRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0)
    quantity: int = Field(default=0)
    ingredient: str = Field(default="")
    partial_update_fields: typing.List[str] = Field(default_factory=list)


class IngredientForCraftRequest(BaseModel):
    id: typing.Optional[int] = Field(default=0)
    quantity: int = Field(default=0)
    ingredient: str = Field(default="")


class IngredientForCraftRetrieveRequest(BaseModel):
    id: int = Field(default=0)


class IngredientListRequest(BaseModel):
    pass


class IngredientResponse(BaseModel):
    name: str = Field(default="")
    price: typing.Optional[int] = Field(default=0)


class IngredientListResponse(BaseModel):
    results: typing.List[IngredientResponse] = Field(default_factory=list)


class IngredientPartialUpdateRequest(BaseModel):
    name: str = Field(default="")
    price: typing.Optional[int] = Field(default=0)
    partial_update_fields: typing.List[str] = Field(default_factory=list)


class IngredientRequest(BaseModel):
    name: str = Field(default="")
    price: typing.Optional[int] = Field(default=0)


class IngredientRetrieveRequest(BaseModel):
    name: str = Field(default="")


class MetierDestroyRequest(BaseModel):
    name: str = Field(default="")


class MetierListRequest(BaseModel):
    pass


class MetierResponse(BaseModel):
    name: str = Field(default="")


class MetierListResponse(BaseModel):
    results: typing.List[MetierResponse] = Field(default_factory=list)


class MetierPartialUpdateRequest(BaseModel):
    name: str = Field(default="")
    partial_update_fields: typing.List[str] = Field(default_factory=list)


class MetierRequest(BaseModel):
    name: str = Field(default="")


class MetierRetrieveRequest(BaseModel):
    name: str = Field(default="")


class RecetteDestroyRequest(BaseModel):
    ingredient: str = Field(default="")


class RecetteListRequest(BaseModel):
    pass


class RecetteResponse(BaseModel):
    ingredient: str = Field(default="")
    level: typing.Optional[int] = Field(default=0)
    metier: typing.Optional[str] = Field(default="")
    ingredients: typing.List[int] = Field(default_factory=list)


class RecetteListResponse(BaseModel):
    results: typing.List[RecetteResponse] = Field(default_factory=list)


class RecettePartialUpdateRequest(BaseModel):
    ingredient: str = Field(default="")
    level: typing.Optional[int] = Field(default=0)
    metier: typing.Optional[str] = Field(default="")
    ingredients: typing.List[int] = Field(default_factory=list)
    partial_update_fields: typing.List[str] = Field(default_factory=list)


class RecetteRequest(BaseModel):
    ingredient: str = Field(default="")
    level: typing.Optional[int] = Field(default=0)
    metier: typing.Optional[str] = Field(default="")
    ingredients: typing.List[int] = Field(default_factory=list)


class RecetteRetrieveRequest(BaseModel):
    ingredient: str = Field(default="")


class RuneDestroyRequest(BaseModel):
    name: str = Field(default="")


class RuneListRequest(BaseModel):
    pass


class RuneResponse(BaseModel):
    name: str = Field(default="")
    prix_ra: typing.Optional[int] = Field(default=0)
    prix_pa: typing.Optional[int] = Field(default=0)
    prix_ba: typing.Optional[int] = Field(default=0)


class RuneListResponse(BaseModel):
    results: typing.List[RuneResponse] = Field(default_factory=list)


class RunePartialUpdateRequest(BaseModel):
    name: str = Field(default="")
    prix_ra: typing.Optional[int] = Field(default=0)
    prix_pa: typing.Optional[int] = Field(default=0)
    prix_ba: typing.Optional[int] = Field(default=0)
    partial_update_fields: typing.List[str] = Field(default_factory=list)


class RuneRequest(BaseModel):
    name: str = Field(default="")
    prix_ra: typing.Optional[int] = Field(default=0)
    prix_pa: typing.Optional[int] = Field(default=0)
    prix_ba: typing.Optional[int] = Field(default=0)


class RuneRetrieveRequest(BaseModel):
    name: str = Field(default="")
