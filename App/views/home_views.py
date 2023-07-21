from flask import Blueprint, render_template, redirect, url_for, flash, abort
from models.users import User
from forms.user_forms import LoginForm

home_views = Blueprint('home', __name__)

@home_views.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.get_by_password(email, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            return render_template('home/inicio_sesion.html', user=user)
    return render_template('home/inicio_sesion.html', form=form)
