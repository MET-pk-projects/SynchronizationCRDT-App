import json
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
from py3crdt.gset import GSet
from blueprints.models.node1_model import Node1Model
from typing import Any

from typing import Any, List

class Paxos:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.proposed_value = None
        self.accepted_values: List[Any] = []

    def propose(self, value: Any) -> List[Any]:
        # Check if the proposed value is higher than the currently accepted value
        if self.accepted_values:
            accepted_values_int = [int(value) for value in self.accepted_values if value]

            # Find the maximum value
            current_max = max(accepted_values_int)
        else:
            current_max = None

        if current_max is None or int(value) > int(current_max):

            self.proposed_value = value

            # Simulate sending proposal to acceptors and receiving their responses
            # For simplicity, we'll assume all acceptors accept the proposal
            self.accepted_values.append(value)

        else:
            self.accepted_values.append(current_max)

        return self.accepted_values

NODE_ID = 1
person_names = GSet(id=NODE_ID)
paxos_instance_account = Paxos(node_id=NODE_ID)
async def on_connect(websocket):
    try:
        print('WebSocket connection opened')
        while True:
            data = await websocket.receive() 
            data = json.loads(data)
            if 'account_number' in data:
                account_number = data['account_number']
            else:
                account_number = 0
            if 'person_name' in data:
                person_name = data['person_name']
                person_names.add(person_name)
                
                # Persist the person name in the database
                Node1Model.create(person_name=person_name, account_number=account_number)

                # Use Paxos to reach consensus on the account number
                accepted_account_number = paxos_instance_account.propose(account_number)
                # Persist the person name in the database
              
              
            # Convert the G-Set CRDT to a regular set for sending
            data_person_names = list(person_names.payload)
            await websocket.send(json.dumps({
                'person_names': data_person_names,
                'account_number': accepted_account_number,
            }))

    except ConnectionClosed:
        pass