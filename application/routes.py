from flask import render_template, request, jsonify
from server import app, db
from application import models
from application import template_filters
from application.kabumapi.product_helper import ProductHelper
from application import api

@app.route('/')
def indexView():
    return render_template('index.html', produtos=models.Product.query.all())

@app.route('/api_methodview/')
def apiMethodView():
    return render_template('api_methodview.html')

@app.route('/signals/')
def signalsView():
    return render_template('signals.html', sinais=models.LogException.query.all())

@app.route('/register_product/', methods=['POST'])
def registerProduct():
    textJsonProduct = request.form.get('textJsonProduct')
    productHelper = ProductHelper()
    dataProduct = productHelper.getProductByTextJson(textJsonProduct)
    try:
        product = models.Product(
            nome = dataProduct['nome'],
            preco = dataProduct['preco'],
            preco_prime = dataProduct['preco_prime'],
            preco_antigo = dataProduct['preco_antigo'],
            disponibilidade = dataProduct['disponibilidade'],
            preco_desconto = dataProduct['preco_desconto'],
            preco_desconto_prime = dataProduct['preco_desconto_prime'],
            link_descricao = dataProduct['link_descricao'],
            foto = dataProduct['fotos'][0]
        )
        product.save()
        dataProduct = {
            'id': product.id,
            'nome': product.nome,
            'preco': product.preco,
            'preco_desconto': product.preco_desconto,
            'link_descricao': product.link_descricao,
            'foto': product.foto
        }
        return jsonify({'msg': 'Produto registrado no banco de dados!', 'product': dataProduct}), 200
    except:
        return jsonify({'msg': 'Problema durante o cadastro no banco de dados.'}), 400

@app.route('/delete_product/', methods=['POST'])
def deleteProduct():
    idProduct = request.form.get('idProduct')
    try:
        product = models.Product.query.get(idProduct)
        product.delete()
        return jsonify({'msg': 'Produto deletado com sucesso!'}), 200
    except:
        return jsonify({'msg': 'Problemas ao deletar produto do banco!'}), 400