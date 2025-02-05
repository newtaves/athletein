from flask import Blueprint, render_template, redirect, url_for
from athletein.database.database import get_db
tournament_bp = Blueprint("tournament", __name__, url_prefix="/api")


@tournament_bp.route("/tournament")
def tournament():
    db = get_db()
    return "This is tournament page"