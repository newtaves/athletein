from flask import Flask
def create_app():
    #creating the flask factory
    app = Flask(__name__)

    #Required to set up cookies
    app.config['SECRET_KEY'] = 'secret'

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

