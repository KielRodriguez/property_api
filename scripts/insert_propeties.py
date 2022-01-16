# Python
import os
from random import randrange, choice
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'app'))

# SQLAlquemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

from faker import Faker

from models import Property

load_dotenv(os.path.join(BASE_DIR, ".env"))

fake = Faker()

engine = create_engine(os.environ["DATABASE_URL"])
db_session = sessionmaker(engine)

def get_property():

    model = Property(
        bed = randrange(1,10),
        bath = randrange(1,5),
        parking_spots = randrange(1,5),
        size = choice([100, 120, 130, 200, 220, 250]),
        price = randrange(2000, 15000),
        type = choice(['renta', 'compra', 'ambos'])
    )

    return model


with db_session() as session:
    i = 0

    for i in range(1000):
        property = get_property()
        session.add(property)
        session.commit()
