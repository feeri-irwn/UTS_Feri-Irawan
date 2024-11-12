from flask import jsonify, request
from models.CompanyModel import Company
from config import db

def create_company():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'industry')):
        return jsonify({'message': 'Name and industry are required fields'}), 400
    
    company = Company(
        name=data['name'],
        industry=data['industry']
    )
    
    db.session.add(company)
    db.session.commit()
    
    return jsonify({
        'id': company.id,
        'name': company.name,
        'industry': company.industry
    }), 201

def get_all_companies():
    companies = Company.query.all()
    
    if not companies:
        return jsonify({'message': 'No companies found'}), 404
    
    company_list = [{
        'id': company.id,
        'name': company.name,
        'industry': company.industry
    } for company in companies]
    
    return jsonify(company_list), 200

def get_company(id):
    company = Company.query.get(id)
    
    if company:
        return jsonify({
            'id': company.id,
            'name': company.name,
            'industry': company.industry
        }), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404

def update_company(id):
    company = Company.query.get(id)
    
    if company:
        data = request.get_json()
        
        company.name = data.get('name', company.name)
        company.industry = data.get('industry', company.industry)
        
        db.session.commit()
        
        return jsonify({
            'id': company.id,
            'name': company.name,
            'industry': company.industry
        }), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404

def delete_company(id):
    company = Company.query.get(id)
    
    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': f'Company with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Company with ID {id} not found'}), 404
