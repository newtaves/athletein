from athletein.app import create_app
from athletein.database.database import init_db

def main():
    app = create_app()
    with app.app_context():
        init_db()
    app.run(debug=True)


if __name__=="__main__":
    main()
