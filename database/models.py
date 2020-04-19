from .db import db


class Advert(db.Document):
    title = db.StringField(required=True, unique=False)
    comments = db.ListField(db.StringField(), required=True)
    tags = db.ListField(db.StringField(), required=True)
