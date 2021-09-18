from kodpanik.modules.posts.serializers import post_serializer, posts_serializer


def test_post_serializer(post_factory):
    post = post_factory()
    serializer = post_serializer.dump(post)
    assert serializer


def test_posts_serializer(post_factory):
    posts = post_factory.create_batch(10)
    serializers = posts_serializer.dump(posts)
    assert serializers
