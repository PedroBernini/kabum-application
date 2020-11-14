from flask.views import MethodView
from server import app
from flask import jsonify
from application import models

class ProductAPI(MethodView):

    def get(self, product_id):
        if product_id is None:
            products = [product.serialize() for product in models.Product.query.all()]
            return jsonify({'msg': 'Sucesso!', 'products': str([str(product) + '\n' for product in products])}), 200
        else:
            try:
                return jsonify({'msg': 'Sucesso!', 'product': str(models.Product.query.get(product_id).serialize())}), 200
            except:
                return jsonify({'msg': 'Não existe nenhum produto com este ID!'}), 400

product_view = ProductAPI.as_view('product_api')

app.add_url_rule('/product/', defaults={'product_id': None},
                view_func=product_view, methods=['GET',])
app.add_url_rule('/product/<int:product_id>',
                view_func=product_view, methods=['GET'])