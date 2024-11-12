from flask import jsonify, request
from models.CompanyModel import Company
from config import db

# Function to create a new company
def create_company():
    # Get the data from the request body (JSON format)
    data = request.get_json()
    
    # Validate the data
    if not data or not all(k in data for k in ('name', 'industry')):
        return jsonify({'message': 'Name and industry are required fields'}), 400
    
    # Create a new Company object using the data passed in
    company = Company(
        name=data['name'],
        industry=data['industry']
    )
    
    # Add the new company to the session and commit it to the database
    db.session.add(company)
    db.session.commit()
    
    # Return the created company object as JSON
    return jsonify({
        'id': company.id,
        'name': company.name,
        'industry': company.industry
    }), 201

# Function to get all companies
def get_all_companies():
    # Retrieve all companies from the database
    companies = Company.query.all()
    
    # If no companies found, return a message
    if not companies:
        return jsonify({'message': 'No companies found'}), 404
    
    # Convert each company to a dictionary and return as JSON
    company_list = [{
        'id': company.id,
        'name': company.name,
        'industry': company.industry
    } for company in companies]
    
    return jsonify(company_list), 200

# Function to get a specific company by ID
def get_company(id):
    # Retrieve a specific company based on the provided ID
    company = Company.query.get(id)
    
    if company:
        return jsonify({
            'id': company.id,
            'name': company.name,
            'industry': company.industry
        }), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404

# Function to update an existing company by ID
def update_company(id):
    # Retrieve the company object to update
    company = Company.query.get(id)
    
    if company:
        # Get the data from the request body
        data = request.get_json()
        
        # Update the fields with the data provided
        company.name = data.get('name', company.name)
        company.industry = data.get('industry', company.industry)
        
        # Commit the changes to the database
        db.session.commit()
        
        return jsonify({
            'id': company.id,
            'name': company.name,
            'industry': company.industry
        }), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404

# Function to delete a company by ID
def delete_company(id):
    # Retrieve the company to delete
    company = Company.query.get(id)
    
    if company:
        # Delete the company from the session and commit the change
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': f'Company with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404
