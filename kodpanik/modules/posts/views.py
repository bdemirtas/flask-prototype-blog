from flask import Blueprint, request, jsonify

from kodpanik.modules.posts.models import Post, Category
from kodpanik.modules.posts.serializers import post_serializer
from kodpanik.modules.posts.service import service
from kodpanik.utils.validators import pagination_query_params_validator

post_bp = Blueprint('posts', __name__, template_folder='templates')
category_bp = Blueprint('categories', __name__, template_folder='templates')


@post_bp.route("/", methods=["GET"])
def list_posts():
    query_params = pagination_query_params_validator.load(data=request.args)
    posts = service.list_posts(**query_params)
    return jsonify(posts)


@post_bp.route("/<int:id>", methods=["GET"])
def post_detail(id: int):
    post = Post.query.details(id)
    return jsonify(post)


@post_bp.route("/", methods=["POST"])
def create_post():
    data = request.json()
    post = post_serializer.load(data)


@post_bp.route("/<int:id>", methods=["PATCH"])
def patch_post(id: int):
    pass


@post_bp.route("/<int:id>", methods=["PUT"])
def put_post(id: int):
    pass


@post_bp.route("/<int:id>", methods=["DELETE"])
def delete(id: int):
    pass


@category_bp.route("/<int:id>", methods=["GET"])
def category_detail(id: int):
    category = Category.query.details(id)
    return jsonify(category)
