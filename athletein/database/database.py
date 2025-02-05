import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import g, current_app
import os
# Fetch the service account key JSON file (same process as for Realtime Database)
  # Replace with the actual path.

def init_db(config_file):
    cred = credentials.Certificate(config_file)
    firebase_admin.initialize_app(cred) # No need to specify the databaseURL for Firestore.

    db = firestore.client()  # Get a Firestore client
    return db

def get_db():
    """Gets firestore instance and stores it in the g object."""
    if 'db' not in g:
        print("Initializing DB")
        g.db= firestore.client() # Initialize and store it
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

def init_app(app):
    app.teardown_appcontext(close_db)
