from peewee import *
from .base_model import BaseModel


class Node1Model(BaseModel):
    id = AutoField()
    person_name = CharField(max_length=80, null=False)
    account_number = IntegerField()

    def to_dict(self):
        return {
            "person_name": str(self.person_name),
            "account_number" : str(self.account_number)
        }

    class Meta:
        db_table = "node1"

