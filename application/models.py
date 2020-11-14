from server import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

class BaseModel():

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Product(db.Model, BaseModel, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    preco_prime = db.Column(db.Float, nullable=True)
    preco_antigo = db.Column(db.Float, nullable=True)
    disponibilidade = db.Column(db.Boolean, default=False)
    preco_desconto = db.Column(db.Float, nullable=True)
    preco_desconto_prime = db.Column(db.Float, nullable=True)
    link_descricao = db.Column(db.String(300), nullable=True)
    foto = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return '<Produto %r>' % self.nome

class LogException(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    exception = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Exception %r>' % self.exception