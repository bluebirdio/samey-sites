from sqlalchemy import Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from samey.tables import *
from sites.repositories.values import RepositoryTargetType

from .values import Environment


class Instance(SameyTable):
    url = Column(String(255))

    application_id = Column(
        ForeignKey("application.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    stack_id = Column(
        ForeignKey("stack.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )

    environment = Column(Enum(Environment), nullable=False)

    instance_group = Column(String(255))

    repository_id = Column(
        ForeignKey("repository.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=True,
    )

    repository_target_type = Column(Enum(RepositoryTargetType), nullable=True)

    repository_target = Column(String(255))

    __table_args__ = (
        UniqueConstraint("name", "application_id", name="unique_name_application_id"),
    )
    application = relationship("Application", lazy="subquery")
