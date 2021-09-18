from kodpanik.modules.notifications.models import Message
from kodpanik.modules.posts.controller import controller as posts_controller
from kodpanik.modules.notifications import controller as notification_controller
from kodpanik.modules.posts.serializers import posts_serializer, post_serializer


class Service:

    def __init__(self, posts_controller, notification_controller):
        self.posts_controller = posts_controller
        self.notification_controller = notification_controller

    def list_posts(self, **filters):
        posts = self.posts_controller.list_posts_by_filters(**filters)
        return posts_serializer.dump(posts)

    def get_post(self, id):
        post = self.posts_controller.get_post(id)
        return post_serializer.dump(post)

    def create_post(self, **data):
        msg = Message(
            subject="new post created",
            body="a new post had been created",
            from_email="test@test.com",
            to_email=["test@test.com"]
        )
        self.posts_controller.create_post(**data)
        self.notification_controller.send_notification()


service = Service(posts_controller, notification_controller)
