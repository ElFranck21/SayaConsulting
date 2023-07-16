from flask import Blueprint, render_template, redirect, url_for, flash, abort

from models.users import User

from forms.user_forms import RegisterForm, LoginForm, ProfileForm

from utils.file_handler import save_image

user_views = Blueprint('user', __name__)

@user_views.route('/users/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User(username, password, email)
        user.save()

        return redirect(url_for('user.login'))
    return render_template('users/register.html', form=form)

@user_views.route('/users/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_password(username, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            return render_template('home/inicio_sesion.html', user=user)
    return render_template('users/login.html', form=form)

@user_views.route('/users/<int:id>/profile/', methods=('GET', 'POST'))
def profile(id):
    form = ProfileForm()
    user = User.__get__(id)
    if not user:
        abort(404)
    if form.validate_on_submit():
        user.name = form.name.data
        user.ape_pat = form.ape_pat.data
        user.ape_mat = form.ape_mat.data
        f = form.image.data
        if f:
            user.image = save_image(f, 'images/profiles', user.username)
        user.save()
    form.name.data = user.name
    form.ape_pat.data = user.ape_pat
    form.ape_mat.data = user.ape_mat
    image = user.image
    return render_template('users/profile.html', form=form, image=image)