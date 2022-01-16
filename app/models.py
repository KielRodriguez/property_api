# Python
import datetime
import uuid

# SQLAlchemy
from sqlalchemy import Column, sql
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID, INTEGER, SMALLINT, FLOAT, MONEY, VARCHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql  import func

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    # id = Column(UUID, primary_key=True, index=True, default=uuid4)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    bed = Column(SMALLINT, nullable=False)
    bath = Column(FLOAT, nullable=False)
    parking_spots = Column(SMALLINT, nullable=False)
    size = Column(FLOAT, nullable=False)
    price = Column(FLOAT, nullable=False)
    type = Column(VARCHAR(10), nullable=False)