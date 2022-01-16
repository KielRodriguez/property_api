# Python
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field


class Property(BaseModel):
    id: Optional[UUID] = Field(
        default=None
    )
    bed: int = Field(
        ...,
        gt=0
    )
    bath: float = Field(
        ...,
        gt=0
    )
    parking_spots: Optional[int] = Field(
        default=None
    )
    size: float = Field(
        ...,
        gt=0
    )
    price: float = Field(
        ...,
        gt=0
    )

    class Config:
        orm_mode = True