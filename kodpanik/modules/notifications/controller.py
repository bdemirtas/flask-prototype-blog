import dataclasses
import json

from flask_mailman import EmailMessage

from kodpanik.core import db
from kodpanik.modules.notifications.models import Message, MessageLog


class Controller:
    def send_notification(self, message: Message):
        msg = EmailMessage(
            subject=message.subject,
            body=message.body,
            from_email=message.from_email,
            to=message.to_email,
            bcc=message.bcc_email,
            reply_to=message.reply_to,
            headers=message.headers,
        )
        msg.send()
        return self.message_log(message)

    def message_log(self, message):
        data = json.dumps(dataclasses.asdict(message))
        msg = MessageLog(data=data)
        db.session.add(msg)
        db.session.commit()
        return msg


controller = Controller()
