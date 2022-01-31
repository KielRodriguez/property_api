# Python
from enum import Enum
from typing import List, Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field

class PropertyType(Enum):
    rent= "renta"
    purchase= "compra"
    both= "ambos"

class PropertyBase(BaseModel):
    bed: int = Field(...)
    bath: float = Field(...)
    parking_spots: Optional[int] = Field(default=None)
    size: float = Field(...)
    price: float = Field(...)
    type: PropertyType = Field(...)

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: UUID
    owner_id: UUID

    class Config:
        orm_mode = True

# Owner
class OwnerBase(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)

class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: Optional[UUID]
    properties: List[Property]

    class Config:
        orm_mode = True