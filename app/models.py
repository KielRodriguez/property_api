from uuid import uuid4

# SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID, INTEGER, SMALLINT, FLOAT, MONEY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    id = Column(UUID, primary_key=True, index=True, default=uuid4)
    bed = Column(SMALLINT, nullable=False)
    bath = Column(FLOAT, nullable=False)
    parking_spots = Column(SMALLINT, nullable=False)
    size = Column(FLOAT, nullable=False)
    price = Column(MONEY, nullable=False)
    # images
    # renta, compra o ambos casos.