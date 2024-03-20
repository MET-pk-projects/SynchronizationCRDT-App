import asyncio
from websockets import serve
from quart import Quart, websocket
from blueprints.models.node1_model import Node1Model
from blueprints.post_node1 import post_node1_blueprint
from blueprints.get_node1 import get_node1_blueprint
from websocket_node1 import on_connect

app = Quart(__name__)
app.register_blueprint(post_node1_blueprint)
app.register_blueprint(get_node1_blueprint)

def create_tables():
    Node1Model.drop_table(safe=True)
    Node1Model.create_table(safe=True)

    Node1Model.get_or_create(
        id=1,
        person_name="Sohaib",
    )

database = 'database.db'
Node1Model._meta.database.init(database)
create_tables()

@app.websocket('/ws')
async def ws():
    websocket_ = websocket._get_current_object()
    print('WebSocket connection opened')
    await on_connect(websocket_)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8070)

