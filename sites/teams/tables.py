from sqlalchemy import ForeignKey

from samey.tables import *


class Team(TextIdentified, SameyTable, HasDescription):
    pass


class TeamMember(SameyTable):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    role_id = Column(
        ForeignKey("role.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
