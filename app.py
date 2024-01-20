import os
import requests
import logging
import numpy as np
from flask_wtf import Form
from flask_cors import CORS
from flask import Flask
from datetime import datetime
from flask_restful import Api, Resource
from wtforms import StringField, validators
from flask import Flask, Response, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful_swagger_3 import swagger, Resource, Api as SwaggerApi


app = Flask(__name__)
CORS(app)
api_restful = SwaggerApi(app)
api = Api(app)

logging.basicConfig(filename='app.log', level=logging.DEBUG)
# Exemplo de classe de exceção personalizada
class ViaCepError(Exception):
    pass

class CepForm(StringField):
    validators = [validators.Length(min=8, max=10)]


#Endpoint para consultar o Cep na ViaCep
@app.route('/api/consulta-cep/<cep>', methods=['GET'])
def consulta_cep(cep):
    try:
        via_cep_url = f'https://viacep.com.br/ws/{cep}/json/'
        logging.debug(f'Solicitação URL: {via_cep_url}')

        response = requests.get(via_cep_url)

        if response.status_code == 200:
            logging.error('Solicitação Bem Sucedida')
            return jsonify(response.json())
        else:
            logging.error(f'Erro na solicitação. Código de status: {response.status_code}')
            raise ViaCepError('Erro ao consultar o CEP')

    except ViaCepError as e:
        logging.error(f'Exceção personalizada: {str(e)}')
        return jsonify({'erro': 'Erro ao consultar o CEP'}), 500

    except Exception as e:
        logging.error(f'Exceção não tratada: {str(e)}')
        return jsonify({'erro': 'Erro interno do Servidor'}), 500



# Dados de exemplo (simulando um banco de dados)
pedidos = [
    {"id": 1, "produto": "Produto A", "quantidade": 100, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 2, "produto": "Produto B", "quantidade": 10, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 3, "produto": "Produto C", "quantidade": 20, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 4, "produto": "Produto D", "quantidade": 45, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 5, "produto": "Produto F", "quantidade": 230, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 100, "produto": "Produto Z", "quantidade": 1025, "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
]

class PedidosResource(Resource):

    def get(self):
        data = {"pedidos": pedidos}
        return jsonify(data)

    def post(self):
        novo_pedido = request.json
        novo_pedido['id'] = len(pedidos) + 1
        novo_pedido['data_hora'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pedidos.append(novo_pedido)
        return jsonify({"mensagem": "Pedido criado com sucesso"}), 201

    def put(self, pedido_id):
        pedido_id -= 1
        if 0 <= pedido_id < len(pedidos):
            pedido_atualizado = request.json
            pedidos[pedido_id].update(pedido_atualizado)
            return jsonify({"mensagem": "Pedido atualizado com sucesso"}), 200
        else:
            return jsonify({"mensagem": "Pedido não encontrado"}), 404
    
    def delete(self, pedido_id):
        pedido_id -= 1
        if 0 <= pedido_id < len(pedidos):
            del pedidos[pedido_id]
            return jsonify({"mensagem": "Pedido excluído com sucesso"}), 200
        else:
            return jsonify({"mensagem": "Pedido não encontrado"}), 404


# Configuração do Swagger
SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Documentation"}
)

@app.route('/api/swagger.json', methods=['GET'])
def swagger_json():
    return jsonify({"swagger": "2.0", "info": {"title": "API Documentation", "version": "1.0"}})

api_restful.add_resource(PedidosResource, '/api/pedidos')
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


#ApiRestFul Posto-Combustíveis
# Simulação de uma lista de combustíveis (substitua por um banco de dados 
combustiveis = [
    {"id": 1, "tipo": "Gasolina", "quantidade": 3, "preco": 5.0, "valor_total": 15, "operador": 'Ana', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 2, "tipo": "Álcool", "quantidade": 5,  "preco": 4.5, "valor_total": 22.5, "operador": 'Maria', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 3, "tipo": "Diesel", "quantidade": 7,  "preco": 4.0, "valor_total": 28, "operador": 'João', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 4, "tipo": "Gasolina", "quantidade": 10, "preco": 5.0, "valor_total": 50, "operador": 'Fulano', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 5, "tipo": "Álcool", "quantidade": 5,  "preco": 4.5, "valor_total": 22.5, "operador": 'Beltrano', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
    {"id": 6, "tipo": "Diesel", "quantidade": 100,  "preco": 4.0, "valor_total": 400, "operador": 'Ciclano', "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
]

# Rotas CRUD para combustíveis
@app.route('/combustiveis', methods=['GET'])
def get_combustiveis():
    return jsonify(combustiveis)

@app.route('/combustiveis/<int:combustivel_id>', methods=['GET'])
def get_combustivel(combustivel_id):
    combustivel = next((c for c in combustiveis if c['id'] == combustivel_id), None)
    
    if combustivel is None:
        return jsonify({'error': 'Combustível não encontrado'}), 404
    
    return jsonify(combustivel)

@app.route('/combustiveis', methods=['POST'])
def adicionar_combustivel():
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    novo_combustivel = {
        "id": len(combustiveis) + 1,
        "tipo": request.json.get('tipo'),
        "quantidade": request.json.get('quantidade'),
        "preco": request.json.get('preco'),
        "valor_total": float(request.json.get('quantidade')) * float(request.json.get('preco')),
        "operador": request.json.get('operador'),
        "data_hora": data_atual
    }

    combustiveis.append(novo_combustivel)

    return jsonify({"mensagem": "Combustível adicionado com sucesso", "combustivel": novo_combustivel}), 201

@app.route('/combustiveis/<int:combustivel_id>', methods=['PUT'])
def atualizar_combustivel(combustivel_id):
    for combustivel in combustiveis:
        if combustivel['id'] == combustivel_id:
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Atualize os campos conforme necessário
            combustivel['quantidade'] = request.json.get('quantidade', combustivel['quantidade'])
            combustivel['preco'] = request.json.get('preco', combustivel['preco'])
            try:
            	combustivel['valor_total'] = float(combustivel['quantidade']) * float(combustivel['preco'])
            except (ValueError, IndexError) as e:
            	print(f"Erro ao converter valores: {e}")
		    
            combustivel['data_hora'] = data_atual

            return jsonify({"mensagem": "Combustível atualizado com sucesso", "combustivel": combustivel}), 200

    return jsonify({"mensagem": "Combustível não encontrado"}), 404

@app.route('/combustiveis/<int:combustivel_id>', methods=['DELETE'])
def delete_combustivel(combustivel_id):
    global combustiveis
    combustiveis = [c for c in combustiveis if c['id'] != combustivel_id]
    return jsonify({'message': 'Combustível excluído com sucesso'})


if __name__ == '__main__':
	app.run(debug=True)
