from flask_restful import Resource, reqparse

from commons.headers_cheker import secret_required, admin_only
from model.spec import SpecModel

_spec_parser = reqparse.RequestParser()
_spec_parser.add_argument('spec_name', type=str, required=True, help="Параметр spec_name не может быть пустым")
_spec_parser.add_argument('code', type=str, required=True, help="Параметр code не может быть пустым")


class Spec(Resource):
    @classmethod
    @secret_required
    def get(cls, spec_id):
        user = SpecModel.find_by_id(spec_id)
        if not user:
            return {'message': 'Spec not found'}, 404
        return user.json()


class SpecCreate(Resource):
    @classmethod
    @secret_required
    @admin_only
    def put(cls):
        data = _spec_parser.parse_args()
        spec = SpecModel(**data)
        spec.save_to_db()
        return spec.json(), 201


class SpecList(Resource):
    @classmethod
    @secret_required
    def get(cls):
        spec_list = SpecModel.find_all()
        return [spec.json() for spec in spec_list]
