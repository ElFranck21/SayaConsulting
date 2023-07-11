
from flask import (Flask, render_template, request, 
redirect, flash, url_for)
#Importar  Clases de DataBase
#from db.categories import Category
#from db.users import User
#Importar formularios
#from forms.users_forms import CreateUserForm
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'My Secret Key'
@app.route('/')
@app.route('/inicio_sesion/')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/sesion_admin/')
def sesion_admin():
    return render_template('sesion_admin.html')

@app.route('/usuario/')
def usuario():
    return render_template('usuario.html')

@app.route('/proveedor/')
def proveedor():
    return render_template('proveedor.html')

@app.route('/maquilador/')
def maquilador():
    return render_template('maquilador.html')
@app.route('/maquileros/')
def maquileros():
    return render_template('maquileros.html')
@app.route('/puestos/')
def puestos():
    return render_template('puestos.html')
@app.route('/tela/')
def tela():
    return render_template('tela.html')
@app.route('/producto/')
def producto():
    return render_template('producto.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

@app.route('/users/create')
def create_user():
    form = CreateUserForm()
    return render_template('create_user.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)