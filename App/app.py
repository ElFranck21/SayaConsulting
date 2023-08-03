from flask import Flask

# Importar Views
from views.home_views import home_views
from views.admin_views import admin_views
from views.entry_views import entry_views
from views.error_views import error_views
from views.text_views import text_views
from views.user_views import user_views
from views.supplier_views import supplier_views
from views.maquilero_views import maquilero_views
from views.maquilador_views import maquilador_views
from views.position_views import position_views
from views.type_of_material_views import material_views
from views.product_views import product_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

# Registrar Views
app.register_blueprint(home_views)
app.register_blueprint(admin_views)
app.register_blueprint(entry_views)
app.register_blueprint(error_views)
app.register_blueprint(text_views)
app.register_blueprint(user_views)
app.register_blueprint(supplier_views)
app.register_blueprint(maquilero_views)
app.register_blueprint(maquilador_views)
app.register_blueprint(position_views)
app.register_blueprint(material_views)
app.register_blueprint(product_views)

if __name__ == '__main__':
    app.run(debug=True)