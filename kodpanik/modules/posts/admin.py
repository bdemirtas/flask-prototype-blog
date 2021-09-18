from flask_admin.contrib.sqla import ModelView


class PostAdmin(ModelView):
    column_display_pk = True


class CategoryAdmin(ModelView):
    column_display_pk = True
