import factory
import pytest
from faker import Faker

from kodpanik.modules.notifications.models import Message, MessageLog
from kodpanik.modules.notifications import controller


faker = Faker()


@pytest.fixture
def messagelog_factory(session):
    class MessageLogFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = MessageLog
            sqlalchemy_session = session
            sqlalchemy_session_persistence = "commit"
        from_email = faker.email()
        data = dict(
            subject=faker.word(),
            body=faker.text(),
            from_email=from_email,
            to_email=[faker.email(), faker.email()],
            bcc_email=[faker.email(), faker.email()],
            reply_to=[from_email],
            headers={},
        )

    return MessageLogFactory


class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    subject = faker.email()
    body = faker.text()
    from_email = faker.email()
    to_email = [faker.email()]
    bcc_email: [faker.email()]
    reply_to: [from_email]
    headers = {}


@pytest.fixture
def notification_controller(session):
    return controller
