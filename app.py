from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource, reqparse

# Crear la aplicación Flask
app = Flask(__name__)
api = Api(app)

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Leche", "precio": 15.0},
    {"id": 2, "nombre": "Pan", "precio": 10.0}
]

# Creando el Blueprint para los productos
productos_bp = Blueprint('productos', __name__)

# Clase para manejar la ruta de productos
class ProductoResource(Resource):
    def get(self):
        return jsonify(productos)

    def post(self):
        # Parseo de los datos para agregar un nuevo producto al carrito
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help="ID del producto es obligatorio")
        parser.add_argument('nombre', type=str, required=True, help="Nombre del producto es obligatorio")
        parser.add_argument('precio', type=float, required=True, help="Precio del producto es obligatorio")

        args = parser.parse_args()

        # Agregar el producto al carrito (en este caso solo simula)
        nuevo_producto = {
            'id': args['id'],
            'nombre': args['nombre'],
            'precio': args['precio']
        }

        # Lógica para agregarlo a un "carrito" (en este caso solo en memoria)
        productos.append(nuevo_producto)

        return jsonify({"mensaje": "Producto agregado al carrito", "producto": nuevo_producto})

# Registrar las rutas
api.add_resource(ProductoResource, '/productos')

# Ruta raíz para confirmar que el servicio está corriendo
@app.route('/')
def index():
    return "Bienvenido a la Tiendita API!"

# Registrar el Blueprint
app.register_blueprint(productos_bp, url_prefix='/api')

if __name__ == '__main__':
    # Ejecutar la aplicación en el modo de desarrollo para pruebas locales
    app.run(debug=True)
