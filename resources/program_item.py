from flask_restful import Resource, reqparse

from commons.headers_cheker import secret_required, admin_only
from model.program_item import ProgramItemModel


class ProgramItem(Resource):
    @classmethod
    @secret_required
    def get(cls, pi_id):
        program_item = ProgramItemModel.find_by_id(pi_id)
        if not program_item:
            return {'message': 'Program item not found'}, 404
        return program_item.json()


class ProgramItemList(Resource):
    @classmethod
    @secret_required
    def get(cls):
        program_item_list = ProgramItemModel.find_all()
        return [pi.json() for pi in program_item_list]