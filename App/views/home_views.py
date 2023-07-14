from flask import Blueprint, render_template

home_views = Blueprint('home', __name__)

@home_views.route('/')
@home_views.route('/inicio_sesion/')
def inicio_sesion():
    return render_template('home/inicio_sesion.html')
