# Kabum Application
Basic Flask Application

# Como rodar o projeto?
Antes de rodar o projeto pela primeira vez, é necessário criar as tabelas da aplicação no banco de dados. Para isso, importe o objeto *db* do arquivo *server.py* e utilize o método *create_all()* do mesmo para realizar a criação.
**Exemplo no terminal:**
**$ from server import db**
**$ db.create_all()**

Após a criação das tabelas, utilize o arquivo *wsgi.py* para iniciar o servidor.
**Exemplo no terminal:**
**$ python wsgi.py**

Utilize o servidor da aplicação (http://localhost:5000/) através de algum navegador.
