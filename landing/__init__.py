from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
#import os
#print(str(os.getcwd()))


UPLOAD_FOLDER = "../uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.secret_key = 'somesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER                     # new
db = SQLAlchemy(app)
manager = LoginManager(app)


from landing import models, routes


admin = Admin(app, index_view=models.MyAdminIndexView())
admin.add_view(models.MyModelView(models.User, db.session))
admin.add_view(models.MyModelView(models.Message, db.session))
admin.add_view(models.MyModelView(models.Tag, db.session))

#db.create_all()
