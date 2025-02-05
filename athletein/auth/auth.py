from flask import render_template, request, url_for, g, flash, Blueprint, session, redirect, jsonify, make_response
from athletein.database.models import User
from athletein.database.database import get_db


auth_bp = Blueprint('auth',__name__, url_prefix='/api')


@auth_bp.route('/signup', methods=['POST'])
def signup():
    db = get_db()
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        if not name or not password or not email:
            return jsonify({'status':'error','message':'email or password or name not provided.'}), 400
        new_user = User(db)
        return jsonify(new_user.add_user(name, password, email))
    else:
        return jsonify({'status':'error','message':'method not allowed'}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        data = request.get_data()
        email = request.form.get('email')
        password = request.form.get('password')

        if not password or not email:
            return jsonify({'status':'error','message':'email or password not provided.'}), 400
        user = User(db)
        pass_match = user.check_password(email, password)

        if pass_match.get('status')=='success':
            return jsonify(user.get_user_by_id(pass_match.get('user_id')))
        else:
            return jsonify(pass_match)
    else:
        return jsonify({'status':'error','message':'method not allowed'}), 400

@auth_bp.route('/logout')
def logout():
    # session.clear()
    return redirect(url_for('views.views'))