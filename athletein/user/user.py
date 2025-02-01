from flask import Blueprint, render_template, redirect, url_for

user_bp = Blueprint("user", __name__, url_prefix="/user")



@user_bp.route("/profile")
def home():
    return "This is userpage"