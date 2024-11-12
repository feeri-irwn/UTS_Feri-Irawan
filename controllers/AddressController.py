from flask import jsonify, request
from models.AddressModel import Address
from config import db

def create_address():
    data = request.get_json()
    

    if not data or not all(k in data for k in ('street', 'city', 'state', 'zip_code')):
        return jsonify({'message': 'Error: Missing required fields (street, city, state, zip_code). Please provide all required data.'}), 400

    address = Address(
        street=data['street'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code']
    )
    
    db.session.add(address)
    db.session.commit()
    
    return jsonify({
        'message': 'Address created successfully!',
        'id': address.id,
        'street': address.street,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code
    }), 201


def get_all_addresses():
    addresses = Address.query.all()
    
    if not addresses:
        return jsonify({'message': 'No addresses found in the database.'}), 404
    
    address_list = [{
        'id': address.id,
        'street': address.street,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code
    } for address in addresses]
    
    return jsonify({
        'message': 'Addresses retrieved successfully.',
        'addresses': address_list
    }), 200


def get_address(id):
    address = Address.query.get(id)
    
    if address:
        return jsonify({
            'message': 'Address retrieved successfully.',
            'id': address.id,
            'street': address.street,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code
        }), 200
    
    return jsonify({'message': f'Address with ID {id} not found. Please check the ID and try again.'}), 404


def update_address(id):
    address = Address.query.get(id)
    
    if address:
        data = request.get_json()
        
        address.street = data.get('street', address.street)
        address.city = data.get('city', address.city)
        address.state = data.get('state', address.state)
        address.zip_code = data.get('zip_code', address.zip_code)
        

        db.session.commit()
        
        return jsonify({
            'message': f'Address with ID {id} updated successfully.',
            'id': address.id,
            'street': address.street,
            'city': address.city,
            'state': address.state,
            'zip_code': address.zip_code
        }), 200
    
    return jsonify({'message': f'Address with ID {id} not found. Cannot update a non-existing address.'}), 404

def delete_address(id):
    address = Address.query.get(id)
    
    if address:
        db.session.delete(address)
        db.session.commit()
        return jsonify({'message': f'Address with ID {id} deleted successfully.'}), 200
    
    return jsonify({'message': f'Address with ID {id} not found. Cannot delete a non-existing address.'}), 404
