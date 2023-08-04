from flask import Blueprint, render_template
from models.users import User
from models.supplier import Supplier
from models.maquiladores import Maquilador
from models.maquilero import Maquilero
from models.positions import Position
from models.type_of_material import TypeOfMaterial
from models.product import Product
admin_views = Blueprint('admin', __name__)

@admin_views.route('/sesion_admin/')
def sesion_admin():
    product = Product.get_all()
    return render_template('admin/sesion_admin.html', product=product)

@admin_views.route('/usuario/')
def usuario():
    users = User.get_all()
    return render_template('admin/usuario.html', users=users)

@admin_views.route('/proveedor/')
def proveedor():
    supplier = Supplier.get_all()
    return render_template('admin/proveedor.html', supplier=supplier)
@admin_views.route('/maquilador/')
def maquilador():
    maquilador = Maquilador.get_all()
    return render_template('admin/maquilador.html', maquilador=maquilador)
@admin_views.route('/maquilero/')
def maquilero():
    maquilero = Maquilero.get_all()
    return render_template('admin/maquilero.html', maquilero=maquilero)
@admin_views.route('/puestos/')
def puestos():
    positions = Position.get_all()
    return render_template('admin/puestos.html', positions=positions)
@admin_views.route('/tela/')
def tela():
    type_of_material = TypeOfMaterial.get_all()
    return render_template('admin/tela.html', type_of_material=type_of_material)
@admin_views.route('/producto/')
def producto():
    product = Product.get_all()
    return render_template('admin/producto.html', product=product)