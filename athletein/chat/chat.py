from flask import Blueprint, render_template, redirect, url_for

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")



@chat_bp.route("/")
def home():
    return "This is chatpage"