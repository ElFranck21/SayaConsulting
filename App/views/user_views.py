# user_views.py
from flask import Blueprint, render_template, redirect, url_for
from models.users import User, Position, Role
from forms.user_forms import RegisterForm

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
        name = form.name.data
        direction = form.direction.data
        ape_pat = form.ape_pat.data
        ape_mat = form.ape_mat.data

        # Crear una instancia de User con los datos del formulario
        user = User(ape_mat, ape_pat, direction, email, id_position, id_role, name, image, password, username)

        # Guardar el usuario en la base de datos utilizando el método save()
        user.save()

        return redirect(url_for('admin.usuario'))

    return render_template('users/register.html', form=form)
