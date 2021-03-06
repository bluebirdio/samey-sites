from sqlalchemy import ForeignKey

from samey.tables import *


class Stack(TextIdentified, SameyTable, HasDescription):
    parent_stack_id = Column(
        ForeignKey(
            "stack.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
            use_alter=True,
            name="fk_stack_parent_stack_id",
        ),
        nullable=True,
    )


# Todo versions? major/minor? inheritance?
# Requirements e.g. database, php other environments.
# Related stacks e.g. solr...?
# Job specifications e.g. cron (these implementations would come from somewhere else ofc)
