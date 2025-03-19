from flask import request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from models import db, User, Product
from app import app
from sqlalchemy.exc import IntegrityError

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if not all(k in data for k in ("name", "username", "password")):
        return jsonify({'message': 'Missing data'}), 400
    try:
        new_user = User(name=data['name'], username=data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists!'}), 409

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user and check_password_hash(user.password, data.get('password')):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(minutes=10))
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.name = data.get('name', user.name)
    user.username = data.get('username', user.username)
    if 'password' in data:
        user.set_password(data['password'])
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@app.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.json
    new_product = Product(
        pname=data['pname'],
        description=data.get('description'),
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully!'})

@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            'pid': p.pid,
            'pname': p.pname,
            'description': p.description,
            'price': float(p.price),
            'stock': p.stock,
            'created_at': str(p.created_at)
        } for p in products
    ])

@app.route('/products/<int:pid>', methods=['GET'])
@jwt_required()
def get_product(pid):
    product = Product.query.get_or_404(pid)
    return jsonify({
        'pid': product.pid,
        'pname': product.pname,
        'description': product.description,
        'price': float(product.price),
        'stock': product.stock,
        'created_at': str(product.created_at)
    })

@app.route('/products/<int:pid>', methods=['PUT'])
@jwt_required()
def update_product(pid):
    product = Product.query.get_or_404(pid)
    data = request.json
    product.pname = data.get('pname', product.pname)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

@app.route('/products/<int:pid>', methods=['DELETE'])
@jwt_required()
def delete_product(pid):
    product = Product.query.get_or_404(pid)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})