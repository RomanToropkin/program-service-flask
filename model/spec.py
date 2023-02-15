from db import db

association_table = db.Table(
    "spec_program_item",
    db.Model.metadata,
    db.Column("id_spec", db.ForeignKey("program.spec.id")),
    db.Column("id_program", db.ForeignKey("program.program_item.id")),
    schema="program"
)


class SpecModel(db.Model):
    __tablename__ = 'spec'
    __table_args__ = {"schema": "program"}

    id = db.Column(db.Integer, db.Identity(),
                   primary_key=True)
    spec_name = db.Column(db.String(255))
    code = db.Column(db.String(20))
    program_items = db.relationship("ProgramItemModel", secondary=association_table)

    def __init__(self, spec_name, code):
        self.spec_name = spec_name
        self.code = code

    def json(self):
        return {
            'id': self.id,
            'spec_name': self.spec_name,
            'code': self.code,
            'program_items': self.get_program_items()
        }

    def get_program_items(self):
        return [program_item.json() for program_item in self.program_items]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()