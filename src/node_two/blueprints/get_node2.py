import json
from quart import Blueprint, Response, request
from .models.node2_model import Node2Model

get_node2_blueprint = Blueprint('get_node2', __name__)

@get_node2_blueprint.route('/api/v1/node2', methods=['GET'])
async def get_node1():
    try:
        data = Node2Model.select().dicts()
        data_list = list(data)

        print("Data from database:", data_list)  # for debugging

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(data_list)
        )

    except Exception as e:
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Internal Server Error']
            })
        )
