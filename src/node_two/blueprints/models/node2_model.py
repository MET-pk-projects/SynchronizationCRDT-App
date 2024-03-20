from peewee import *
from .base_model import BaseModel


class Node2Model(BaseModel):
    id = AutoField()
    person_name = CharField(max_length=80, null=False)

    def to_dict(self):
        return {
            "person_name": str(self.person_name)
        }

    class Meta:
        db_table = "node2"

