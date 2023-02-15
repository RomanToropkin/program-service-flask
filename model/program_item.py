from db import db


class ProgramItemModel(db.Model):
    __tablename__ = 'program_item'
    __table_args__ = {"schema": "program"}

    id = db.Column(db.Integer, db.Identity(),
                   primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
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
