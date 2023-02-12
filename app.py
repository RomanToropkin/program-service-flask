from flask import Flask
from flask_restful import Api
from db import db
from resources.spec import Spec, SpecCreate, SpecList

app = Flask(__name__)
app.config.from_pyfile('settings.py')
api = Api(app)  # Flask REST Api code

api.add_resource(Spec, "/spec/<int:spec_id>")
api.add_resource(SpecCreate, "/spec/")
api.add_resource(SpecList, '/spec/')

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9901)
