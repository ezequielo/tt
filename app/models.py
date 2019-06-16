from app.app import db


class CommunityModel(db.Document):
    name = db.StringField(max_length=120, required=True)
    description = db.StringField(required=True)
    manager_id = db.StringField(max_length=120, required=True)
    position = db.DictField(required=True)


class EnrollmentModel(db.Document):
    member_id = db.StringField(max_length=120, required=True)
    name = db.StringField(max_length=120, required=True)
    surname = db.StringField(max_length=120)
    der = db.DictField(required=True)
