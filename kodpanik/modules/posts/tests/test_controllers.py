

def test_list_posts(posts_controller, post_factory, check):
    posts = post_factory.create_batch(5)
    expected_posts = posts_controller.list_posts_by_filters()
    check.equal(len(posts), len(expected_posts))


def test_empty_posts(posts_controller, check):
    expected_posts = posts_controller.list_posts_by_filters()
    check.equal(0, len(expected_posts))


def test_get_post(posts_controller, post_factory, check):
    post = post_factory()
    expected_post = posts_controller.get_post(post.id)
    check.equal(post, expected_post)


def test_get_inexistent(posts_controller, check, faker):
    post = posts_controller.get_post(faker.pyint())
    check.is_none(post)


def test_create_post(posts_controller, check, faker, category_factory):
    category = category_factory()
    data = dict(
        title=faker.sentence(nb_words=5),
        body=faker.text(),
        category_id=category.id
    )
    post = posts_controller.create_post(**data)
    expected_post = posts_controller.get_post(post.id)
    check.equal(post, expected_post)
