import asyncio
from websockets import serve
from quart import Quart, websocket
from blueprints.models.node2_model import Node2Model
from blueprints.post_node2 import post_node2_blueprint
from blueprints.get_node2 import get_node2_blueprint
from websocket_node2 import on_connect

app = Quart(__name__)
app.register_blueprint(post_node2_blueprint)
app.register_blueprint(get_node2_blueprint)

def create_tables():
    Node2Model.drop_table(safe=True)
    Node2Model.create_table(safe=True)

    Node2Model.get_or_create(
        id=1,
        person_name="Andres",
    )

database = 'database.db'
Node2Model._meta.database.init(database)
create_tables()

@app.websocket('/ws')
async def ws():
    websocket_ = websocket._get_current_object()
    print('WebSocket connection opened')
    await on_connect(websocket_)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8070)

