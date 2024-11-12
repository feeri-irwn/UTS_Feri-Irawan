from flask import jsonify, request
from models.AddressModel import Address
from config import db

# Function to create a new address
def create_address():
    # Get the data from the request body
    data = request.get_json()
    
    # Validate the data
    if not data or not all(k in data for k in ('street', 'city', 'state', 'zip_code')):
        return jsonify({'message': 'Error: Missing required fields (street, city, state, zip_code). Please provide all required data.'}), 400

    # Create a new Address object using the data passed in
    address = Address(
        street=data['street'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code']
    )
    
    # Add the new address to the session and commit it to the database
    db.session.add(address)
    db.session.commit()
    
    # Return the created address object as JSON
    return jsonify({
        'message': 'Address created successfully!',
        'id': address.id,
        'street': address.street,
        'city': address.city,
        'state': address.state,
        'zip_code': address.zip_code
    }), 201

# Function to get all addresses
def get_all_addresses():
    # Retrieve all addresses from the database
    addresses = Address.query.all()
    
    # If no addresses are found
    if not addresses:
        return jsonify({'message': 'No addresses found in the database.'}), 404
    
    # Convert each address to a dictionary and return as JSON
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

# Function to get a specific address by ID
def get_address(id):
    # Retrieve a specific address based on the provided ID
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

# Function to update an address by ID
def update_address(id):
    # Retrieve the address object to update
    address = Address.query.get(id)
    
    if address:
        # Get the data from the request body
        data = request.get_json()
        
        # Update the fields with the data provided (only fields provided will be updated)
        address.street = data.get('street', address.street)
        address.city = data.get('city', address.city)
        address.state = data.get('state', address.state)
        address.zip_code = data.get('zip_code', address.zip_code)
        
        # Commit the changes to the database
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

# Function to delete an address by ID
def delete_address(id):
    # Retrieve the address to delete
    address = Address.query.get(id)
    
    if address:
        # Delete the address from the session and commit the change
        db.session.delete(address)
        db.session.commit()
        return jsonify({'message': f'Address with ID {id} deleted successfully.'}), 200
    
    return jsonify({'message': f'Address with ID {id} not found. Cannot delete a non-existing address.'}), 404
