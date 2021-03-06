import re
from datetime import datetime
from uuid import uuid4

import shortuuid
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils.types.uuid import UUIDType


class SameyBaseDBTable:
    @declared_attr
    def __tablename__(self):
        # Generate __tablename__ automatically by turning CamelCase class name to snake_case
        snake = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", self.__name__)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake).lower()

    @declared_attr
    def __table_args__(self):
        return {"mysql_engine": "InnoDB"}

    @hybrid_property
    def id(self):
        try:
            return shortuuid.encode(self.uuid)
        except AttributeError:
            return

    pk = Column(Integer(), primary_key=True)
    uuid = Column(UUIDType(), nullable=False, default=uuid4)
    name = Column(String(255), nullable=False)
    created = Column(DateTime(), default=datetime.utcnow)
    changed = Column(DateTime())

    @id.setter
    def id(self, set_id):
        if set_id is str:
            uuid = shortuuid.decode(set_id)
            if uuid is UUID4:
                self.uuid = shortuuid.decode(set_id)

    def __str__(self):
        return self.name


SameyTable = declarative_base(cls=SameyBaseDBTable)


class TextIdentified:
    id = Column(String(255), nullable=False, index=True, unique=True)


class HasDescription(object):
    description = Column(Text())
