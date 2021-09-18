from kodpanik.modules.notifications.models import MessageLog


def test_send_notification(check, message_factory, notification_controller):
    message = message_factory()
    msg_log = notification_controller.send_notification(message)
    expected_msg_log = MessageLog.query.details(msg_log.id)
    check.equal(msg_log, expected_msg_log)
