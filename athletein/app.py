from flask import Flask,g
from flask_login import LoginManager
from athletein.database.database import init_db, init_app
from firebase_admin import firestore

def create_app():
    #creating the flask factory
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Change this!
    
    #INtialize the database
    init_db(r'.\configs\athletein-c89a8-firebase-adminsdk-fbsvc-215f0df83e.json')

    init_app(app)


    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from athletein.database.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    #Importing blueprints to the flask app
    from athletein.auth.auth import auth_bp
    from athletein.views.views import views_bp
    from athletein.chat.chat import chat_bp
    from athletein.network.network import network_bp
    from athletein.reccomendation.reccomendation import reccomendation_bp
    from athletein.user.user import user_bp

    #Connecting blueprints to the flask_app
    app.register_blueprint(auth_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(network_bp)
    app.register_blueprint(reccomendation_bp)
    app.register_blueprint(user_bp)


    return app

