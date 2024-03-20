import json
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
from py3crdt.gset import GSet
from blueprints.models.node1_model import Node1Model

# Define a unique identifier for the G-Set instance (e.g., node ID)
NODE_ID = 1

# Initialize a G-Set CRDT with the node ID
person_names = GSet(id=NODE_ID)

async def on_connect(websocket):
    try:
        print('WebSocket connection opened')
        while True:
            data = await websocket.receive() 
            data = json.loads(data)

            if 'person_name' in data:
                person_name = data['person_name']
                person_names.add(person_name)

                # Persist the person name in the database
                Node1Model.create(person_name=person_name)

            # Convert the G-Set CRDT to a regular set for sending
            data_to_send = person_names.data
            await websocket.send(json.dumps({
                'person_names': list(data_to_send),
            }))

    except ConnectionClosed:
        pass
