from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Country(db.Model, SerializerMixin):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    population =db.Column(db.Integer)

    def __repr__(self):
        return f'<country: {self.name}, population: {self.population}'~