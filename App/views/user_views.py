# user_views.py
from flask import Blueprint, render_template, redirect, url_for
from models.users import User, Position, Role
from forms.user_forms import RegisterForm

user_views = Blueprint('user', __name__)

@user_views.route('/user/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    positions = Position.get_all()
    form.id_position.choices = [(p.id_position, p.name_position) for p in positions]
    roles = Role.get_all()
    form.id_role.choices = [(r.id_role, r.name_role) for r in roles]

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        ape_mat = form.ape_mat.data
        ape_pat = form.ape_pat.data
        name = form.name.data
        direction = form.direction.data
        id_position = form.id_position.data
        id_role = form.id_role.data

        # Crear una instancia de User con los datos del formulario
        user = User(ape_mat=ape_mat, ape_pat=ape_pat, direction=direction, email=email, id_position=id_position, id_role=id_role, name=name, password=password, username=username)

        # Guardar el usuario en la base de datos utilizando el método save()
        user.save()

        return redirect(url_for('admin.usuario'))

    # Si llegamos aquí, es porque el formulario no ha sido enviado o tiene errores de validación
    # Mostrar los errores en la página
    for field, errors in form.errors.items():
        for error in errors:
            print(f"Error en el campo '{field}': {error}")

    return render_template('users/register.html', form=form)
