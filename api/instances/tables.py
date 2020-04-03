from sqlalchemy import ForeignKey

from api.core.tables import *


class InstanceGroup(TextIdentified, ImprobableDbModel):
    stack_id = Column(
        ForeignKey("stack._id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )
    repository_url = Column(String(255))


class Instance(ImprobableDbModel):
    url = Column(String(255))
    app_id = Column(
        ForeignKey("app._id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    environment_id = Column(
        ForeignKey("environment._id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    instance_group_id = Column(
        ForeignKey("instance_group._id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=True,
    )
