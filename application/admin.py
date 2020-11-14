from server import admin, db
from application import models
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(models.Product, db.session))