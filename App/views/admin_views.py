from flask import Blueprint, render_template

admin_views = Blueprint('admin', __name__)

@admin_views.route('/sesion_admin/')
def sesion_admin():
    return render_template('admin/sesion_admin.html')

@admin_views.route('/usuario/')
def usuario():
    return render_template('admin/usuario.html')

@admin_views.route('/proveedor/')
def proveedor():
    return render_template('admin/proveedor.html')
@admin_views.route('/maquilador/')
def maquilador():
    return render_template('admin/maquilador.html')
@admin_views.route('/maquileros/')
def maquileros():
    return render_template('admin/maquileros.html')
@admin_views.route('/puestos/')
def puestos():
    return render_template('admin/puestos.html')
@admin_views.route('/tela/')
def tela():
    return render_template('admin/tela.html')
@admin_views.route('/producto/')
def producto():
    return render_template('admin/producto.html')