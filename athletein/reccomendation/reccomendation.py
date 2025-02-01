from flask import Blueprint, render_template, redirect, url_for

reccomendation_bp = Blueprint("reccomendation", __name__, url_prefix="/reccomendation")



@reccomendation_bp.route("/")
def home():
    return "This is reccomendation page"