from flask import Blueprint, render_template, redirect, url_for

network_bp = Blueprint("network", __name__, url_prefix="/network")



@network_bp.route("/")
def home():
    return "This is network page"