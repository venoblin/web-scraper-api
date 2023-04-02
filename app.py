from flask import Flask
from flask_restful import Api
from resources.Scrape import Scrape

app = Flask(__name__)
api = Api(app)
api.add_resource(Scrape, '/scrape')
app.run()