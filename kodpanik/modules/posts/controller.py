from kodpanik.core import db
from kodpanik.modules.posts.models import Post, PostStatus


class Controller:
    def list_posts_by_filters(self, page=None, per_page=None, title=None, category=None):
        query = Post.query
        if title:
            query = query.filter(Post.title.like(title))

        if category:
            query = query.filter(Post.category == category)

        if page:
            return query.paginate(page=page, per_page=int(per_page)).items
        return query.all()

    def get_post(self, id):
        return Post.query.details(id)

    def create_post(self, **data):
        post = Post(**data)
        db.session.add(post)
        db.session.commit()
        return post

    def change_post_status(self, id, status):
        """
        draft -> published -> deleted -> archived
        """
        post = self.get_post(id)

        if post.status in [PostStatus.published, PostStatus.deleted, PostStatus.archived] and status == PostStatus.draft:
            return False

        if post.status in [PostStatus.deleted, PostStatus.archived] and status in [PostStatus.draft, PostStatus.published]:
            return False

        if post.status in [PostStatus.archived] and status in [PostStatus.deleted, PostStatus.draft, PostStatus.published]:
            return False

        post.status = status
        db.session.add(post)
        db.session.commit()

        return True, f"Update post status to {status} from {post.status} is denied"


controller = Controller()
