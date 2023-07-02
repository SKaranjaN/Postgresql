import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, make_response, request, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Country

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

api = Api(app)

class Countries(Resource):

    def get(self):
        countries = [country.to_dict() for country in Country.query.all()]
        return make_response(jsonify(countries), 200)

    def post(self):

        data = request.get_json()

        new_country = Country(
            name=data['name'],
            population=data['population'],
        )

        db.session.add(new_country)
        db.session.commit()

        return make_response(new_country.to_dict(), 201)

api.add_resource(Countries, '/countries')

class CountryByID(Resource):
    
    def get(self, id):
        country = Country.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(country), 200)

    def patch(self, id):

        data = request.get_json()

        country = Country.query.filter_by(id=id).first()

        for attr in data:
            setattr(country, attr, data[attr])

        db.session.add(country)
        db.session.commit()

        return make_response(country.to_dict(), 200)

    def delete(self, id):

        country = Country.query.filter_by(id=id).first()
        db.session.delete(country)
        db.session.commit()

        return make_response('', 204)

api.add_resource(CountryByID, '/countries/<int:id>')
