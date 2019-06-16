from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful import Api


db = MongoEngine()


def create_app():

    app = Flask(__name__)

    # db
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tt',
        'host': 'localhost',
        'port': 27017
    }
    db.init_app(app)

    # endpoints
    api = Api(app)
    from app.resources import Community, CommunityEnrollment
    api.add_resource(Community, '/communities', '/communities/<community_name>')
    api.add_resource(CommunityEnrollment, '/communities/<community_name>/enrollments')

    return app
