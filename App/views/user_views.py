from flask import Blueprint, render_template, redirect, url_for
from models.users import User, Position, Role
from models.db import get_connection
from forms.user_forms import RegisterForm, LoginForm, ProfileForm
from utils.file_handler import save_image

user_views = Blueprint('user', __name__)

@user_views.route('/user/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    # Cargar las opciones para el campo position
    positions = Position.get_all()
    form.position.choices = [(position.id_position, position.name_position) for position in positions]
    roles = Role.get_all()
    form.role.choices = [(role.id_role, role.name_role) for role in roles]

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        id_position = form.position.data
        id_role = form.role.data

        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, email, password, id_position, id_role) VALUES (%s, %s, %s, %s, %s)"
        values = (username, email, password, id_position, id_role)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('admin.usuario'))

    return render_template('user/register.html', form=form, positions=positions, roles=roles)