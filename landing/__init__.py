from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = 'somesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
manager = LoginManager(app)


from landing import models, routes


admin = Admin(app, index_view=models.MyAdminIndexView())
admin.add_view(models.MyModelView(models.User, db.session))
admin.add_view(models.MyModelView(models.Message, db.session))
admin.add_view(models.MyModelView(models.Tag, db.session))

#db.create_all()
