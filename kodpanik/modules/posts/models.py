import enum
from datetime import datetime

from kodpanik.core.extensions import db, Base


class PostStatus(enum.Enum):
    draft = "DRAFT"
    published = "PUBLISHED"
    deleted = "DELETED"
    archived = "ARCHIVED"


class Post(Base):
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Enum(PostStatus), nullable=False, default=PostStatus.draft)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("posts", lazy=True))


class Category(Base):
    name = db.Column(db.String(50), nullable=False)
