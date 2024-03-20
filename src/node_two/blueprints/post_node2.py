import json
from quart import Blueprint, Response, request
from .models.node2_model import Node2Model

post_node2_blueprint = Blueprint('post_node2', __name__)

@post_node2_blueprint.route('/api/v1/node2/post', methods=['POST'])
async def post_node2():
    try:
        data = await request.get_json()
        person_name = data.get('person_name') 

        nname = Node2Model.create(person_name=person_name)

        return Response(
            status=200,
            content_type='application/json',
            response=json.dumps(nname.to_dict())
        )

    except Exception as e:
        print(str(e))
        return Response(
            status=500,
            content_type='application/json',
            response=json.dumps({
                'errors': ['Internal Server Error.']
            })
        )
