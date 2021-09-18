from kodpanik.core.extensions import ma
from kodpanik.modules.posts.models import Post, Category


class PostSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_fk = True

    category = ma.HyperlinkRelated("categories.category_detail")


class CategorySerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

    posts = ma.List(ma.HyperlinkRelated("posts.post_detail"))


post_serializer = PostSerializer()
posts_serializer = PostSerializer(many=True)
