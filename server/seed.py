from faker import Faker
import random

from app import app
from models import db, Country

with app.app_context():
    
    fake = Faker()

    Country.query.delete()

    countries = []
    for i in range(50):
        country = Country(
            name=fake.country(),
            population = random.randint(1000000, 10000000000)
        )
        countries.append(country)

    db.session.add_all(countries)
    db.session.commit()