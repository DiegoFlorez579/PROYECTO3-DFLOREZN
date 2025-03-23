from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from models.models import Usuarios
from models.logica import *

routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return f"Bienvenido, {'invitado' if not current_user.is_authenticated else current_user.username}!"


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)  
            return redirect(url_for('routes.index'))
    return render_template('login.html')


@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))


@routes.route('/no_autorizado')
def no_aurorizado():
    return('Lo sentimos, no estas autorizado para ingresar aqui')


@routes.route('/productos')
def productos():
    productos_data = []
    for clave, lista in Heladeria_principal.menu_diario.items():
        for valor in lista:
            productos_data.append(valor.to_dict())
    return jsonify(productos_data)


@routes.route('/producto/<int:producto_id>', methods=['GET'])
@login_required
def obtener_producto_por_id(producto_id):
    if current_user.es_admin or current_user.es_empleado:
        producto = Heladeria_principal.buscar_producto_por_id(producto_id)
        return jsonify(producto.to_dict()) if producto else jsonify({'error': 'Producto no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))
    

@routes.route('/producto/nombre/<string:nombre>', methods=['GET'])
@login_required
def obtener_producto_por_nombre(nombre):
    if current_user.es_admin or current_user.es_empleado:
        producto = Heladeria_principal.buscar_producto_por_nombre(nombre)
        return jsonify(producto.to_dict()) if producto else jsonify({'error': 'Producto no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/producto/calorias/<int:producto_id>', methods=['GET'])
@login_required
def obtener_calorias_producto(producto_id):
    calorias = Heladeria_principal.buscar_calorias_por_id(producto_id)
    return jsonify({'calorias': calorias}) if calorias is not None else jsonify({'error': 'Producto no encontrado'}), 404


@routes.route('/producto/rentabilidad/<int:producto_id>', methods=['GET'])
@login_required
def obtener_rentabilidad_producto(producto_id):
    if current_user.es_admin:
        rentabilidad = Heladeria_principal.consultar_rentabilidad_por_id(producto_id)
        return jsonify({'rentabilidad': rentabilidad}) if rentabilidad is not None else jsonify({'error': 'Producto no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/producto/costo/<int:producto_id>', methods=['GET'])
@login_required
def obtener_costo_produccion_producto(producto_id):
    if current_user.es_admin:
        costo = Heladeria_principal.consultar_costo_produccion_por_id(producto_id)
        return jsonify({'costos': costo}) if costo is not None else jsonify({'error': 'Producto no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/producto/vender/<int:producto_id>', methods=['POST'])
@login_required
def vender_producto(producto_id):
    resultado = Heladeria_principal.vender_producto(producto_id)
    return jsonify({'mensaje': resultado})

@routes.route('/ingredientes', methods=['GET'])
@login_required
def obtener_todos_los_ingredientes():
    if current_user.es_admin or current_user.es_empleado:
        ingredientes = [i.to_dict() for i in Heladeria_principal.consultar_todos_los_ingredientes()]
        return jsonify(ingredientes)
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/ingrediente/<int:ingrediente_id>', methods=['GET'])
@login_required
def obtener_ingrediente_por_id(ingrediente_id):
    if current_user.es_admin or current_user.es_empleado:
        ingrediente = Heladeria_principal.buscar_ingrediente_por_id(ingrediente_id)
        return jsonify(ingrediente.to_dict()) if ingrediente else jsonify({'error': 'Ingrediente no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/ingrediente/nombre/<string:nombre>', methods=['GET'])
@login_required
def obtener_ingrediente_por_nombre(nombre):
    if current_user.es_admin or current_user.es_empleado:
        ingrediente = Heladeria_principal.buscar_ingrediente_por_nombre(nombre)
        return jsonify(ingrediente.to_dict()) if ingrediente else jsonify({'error': 'Ingrediente no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/ingrediente/sano/<int:ingrediente_id>', methods=['GET'])
@login_required
def verificar_ingrediente_sano(ingrediente_id):
    if current_user.es_admin or current_user.es_empleado:
        es_sano = Heladeria_principal.verificar_si_ingrediente_es_sano(ingrediente_id)
        return jsonify({'es_sano': es_sano}) if es_sano is not None else jsonify({'error': 'Ingrediente no encontrado'}), 404
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/producto/reabastecer/<int:producto_id>', methods=['POST'])
@login_required
def reabastecer_producto(producto_id):
    if current_user.es_admin or current_user.es_empleado:
        resultado = Heladeria_principal.reabastecer_producto(producto_id)
        return jsonify({'mensaje': resultado})
    else:
        return redirect(url_for('routes.no_aurorizado'))

@routes.route('/producto/renovar/<int:producto_id>', methods=['POST'])
@login_required
def renovar_inventario_producto(producto_id):
    if current_user.es_admin or current_user.es_empleado:
        cantidad = request.json.get('cantidad', 0)
        resultado = Heladeria_principal.renovar_inventario_producto(producto_id, cantidad)
        return jsonify({'mensaje': resultado})
    else:
        return redirect(url_for('routes.no_aurorizado'))