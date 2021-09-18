from flask import Flask

from kodpanik.core.extensions import db, migrate, ma, admin, mail
from kodpanik.modules.posts.admin import PostAdmin, CategoryAdmin
from kodpanik.modules.posts.views import post_bp as post_bp, category_bp


def create_app(config) -> Flask:
    """
    Creates app with predefined settings that depends on
    environment variable of a system.
    """
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    ma.init_app(app)

    from kodpanik.modules.posts.models import Post, Category

    admin.add_view(PostAdmin(Post, db.session))
    admin.add_view(CategoryAdmin(Category, db.session))

    with app.app_context():
        app.register_blueprint(post_bp, url_prefix="/posts")
        app.register_blueprint(category_bp, url_prefix="/categories")

    return app
