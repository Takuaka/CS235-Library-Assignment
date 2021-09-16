from flask import Blueprint, render_template

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/')
def home():
    return render_template(
        'home/home.html'
    )
