from marshmallow import fields, Schema, validate


class PaginationQueryParamsSchema(Schema):
    page = fields.Int(
        missing=1,
        description='Pagination page number, first page is 1.',
        validate=validate.Range(min=1),
        required=False)
    per_page = fields.Int(
        missing=30,
        description='Pagination items per page.',
        validate=validate.Range(min=3, max=100),
        required=False)


pagination_query_params_validator = PaginationQueryParamsSchema()
