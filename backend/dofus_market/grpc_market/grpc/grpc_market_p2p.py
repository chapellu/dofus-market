# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.2.6.2](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.27.2
# Pydantic Version: 2.8.2
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class IngredientDestroyRequest(BaseModel):
    name: str = Field(default="")


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
    partial_update_fields: typing.List[str] = Field(default_factory=list)
    prix_ra: typing.Optional[int] = Field(default=0)
    prix_pa: typing.Optional[int] = Field(default=0)
    prix_ba: typing.Optional[int] = Field(default=0)


class RuneRequest(BaseModel):
    name: str = Field(default="")
    prix_ra: typing.Optional[int] = Field(default=0)
    prix_pa: typing.Optional[int] = Field(default=0)
    prix_ba: typing.Optional[int] = Field(default=0)


class RuneRetrieveRequest(BaseModel):
    name: str = Field(default="")
