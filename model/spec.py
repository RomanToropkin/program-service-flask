from db import db


class SpecModel(db.Model):
    __tablename__ = 'spec'
    __table_args__ = {"schema": "program"}

    id = db.Column(db.Integer, db.Identity(),
                   primary_key=True)
    spec_name = db.Column(db.String(255))
    code = db.Column(db.String(20))

    def __init__(self, spec_name, code):
        self.spec_name = spec_name
        self.code = code

    def json(self):
        return {
            'id':self.id,
            'spec_name': self.spec_name,
            'code': self.code
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()