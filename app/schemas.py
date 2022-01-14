from uuid import UUID
from pydantic import BaseModel


class Record(BaseModel):
    id: UUID
    bed: int
    bad: float
    parking_spots: int
    size: float
    price: float

    class Config:
        orm_mode = True