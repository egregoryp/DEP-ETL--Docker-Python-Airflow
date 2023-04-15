from flask import Flask, jsonify, request
from api import app
from models.customer_models import Customer
from queries.customer_queries import *
from utils.db import db

# Crea cliente
@app.route('/api/v1/customer', methods=['POST'])
def createCustomer():
    response = create_customer(request.json)
    return jsonify(response)

# Obtiene cliente por id
@app.route('/api/v1/customer/<id>', methods = ['GET'])
def get_customer_by_id(id):
    response = get_customer(id)
    return jsonify(response)

# Actualiza cliente
@app.route('/api/v1/customer/<id>', methods = ['PUT'])
def update_customer_by_id(id):
    response = update_customer(id, request.get_json())
    return jsonify(response)

# Elimina cliente
@app.route('/api/v1/customer/<id>', methods = ['DELETE'])
def delete_customer_by_id(id):
    response = delete_customer(id)
    return jsonify(response)