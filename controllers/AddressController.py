from flask import jsonify, request
from models.AddressModel import Address
from config import db

# Function to create a new address
def create_address(data):
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
    
    # Return the created address object
    return address

# Function to get all addresses
def get_all_addresses():
    # Retrieve all addresses from the database
    addresses = Address.query.all()
    return addresses

# Function to get a specific address by ID
def get_address(id):
    # Retrieve a specific address based on the provided ID
    address = Address.query.get(id)
    return address

# Function to update an address by ID
def update_address(id, data):
    # Retrieve the address object to update
    address = Address.query.get(id)
    
    if address:
        # Update the fields with the data provided
        address.street = data.get('street', address.street)
        address.city = data.get('city', address.city)
        address.state = data.get('state', address.state)
        address.zip_code = data.get('zip_code', address.zip_code)
        
        # Commit the changes to the database
        db.session.commit()
        return address
    return None

# Function to delete an address by ID
def delete_address(id):
    # Retrieve the address to delete
    address = Address.query.get(id)
    
    if address:
        # Delete the address from the session and commit the change
        db.session.delete(address)
        db.session.commit()
        return True
    return False
