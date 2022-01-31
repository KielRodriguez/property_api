# Python
import datetime
import uuid

# SQLAlchemy
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, INTEGER, SMALLINT, FLOAT, MONEY, VARCHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bed = Column(SMALLINT, nullable=False)
    bath = Column(FLOAT, nullable=False)
    parking_spots = Column(SMALLINT, nullable=False)
    size = Column(FLOAT, nullable=False)
    price = Column(FLOAT, nullable=False)
    type = Column(VARCHAR(10), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('owners.id'))
    owner = relationship("Owner", back_populates="properties")

class Owner(Base):
    __tablename__ = "owners"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(VARCHAR(100), nullable=False)
    last_name = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    properties =  relationship("Property", back_populates="owner")