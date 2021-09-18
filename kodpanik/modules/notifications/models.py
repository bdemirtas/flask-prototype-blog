from dataclasses import dataclass, field

from kodpanik.core import db
from kodpanik.core.extensions import Base


@dataclass(frozen=True)
class Message:
    subject: str
    body: str
    from_email: str
    to_email: list[str]
    bcc_email: list[str] = None
    reply_to: list[str] = None
    headers: dict = field(default_factory=dict)


class MessageLog(Base):
    data = db.Column(db.Text, nullable=False)
