from flask import render_template, request, url_for, g, flash, Blueprint, session, redirect

auth_bp = Blueprint('auth',__name__, url_prefix='/auth')



@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    return "This is signup page"


@auth_bp.route('/signin', methods=["GET","POST"])
def signin():
    return "This is signup page"

@auth_bp.route('/logout')
def logout():
    # session.clear()
    return redirect(url_for('main.home'))