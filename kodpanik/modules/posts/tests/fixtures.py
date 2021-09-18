import factory
import pytest

from kodpanik.modules.posts.models import Post, Category, PostStatus
from kodpanik.modules.posts.controller import controller


@pytest.fixture
def post_factory(session, category_factory):
    class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Post
            sqlalchemy_session = session
            sqlalchemy_session_persistence = "commit"

        title = factory.Faker("word")
        status = PostStatus.draft
        body = factory.Faker("word")
        pub_date = factory.Faker("date_time")
        category = factory.SubFactory(category_factory)

    return PostFactory


@pytest.fixture
def category_factory(session):
    class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Category
            sqlalchemy_session = session
            sqlalchemy_session_persistence = "commit"

        name = factory.Faker("word")

    return CategoryFactory


@pytest.fixture
def posts_controller(session):
    return controller
