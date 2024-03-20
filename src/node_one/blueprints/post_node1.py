import json
from quart import Blueprint, Response, request
from .models.node1_model import Node1Model

post_node1_blueprint = Blueprint('post_node1', __name__)

@post_node1_blueprint.route('/api/v1/node1/post', methods=['POST'])
async def post_node1():
    try:
        data = await request.get_json()
        person_name = data.get('person_name') 

        nname = Node1Model.create(person_name=person_name)

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
