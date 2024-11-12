from flask import jsonify, request
from models.EmployeeModel import Employee
from config import db

def create_employee():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('name', 'address_id', 'company_id')):
        return jsonify({'message': 'Name, address_id, and company_id are required fields'}), 400
    
    employee = Employee(
        name=data['name'],
        address_id=data['address_id'],
        company_id=data['company_id']
    )
    
    db.session.add(employee)
    db.session.commit()
    
    return jsonify({
        'id': employee.id,
        'name': employee.name,
        'address_id': employee.address_id,
        'company_id': employee.company_id
    }), 201

def get_all_employees():
    employees = Employee.query.all()
    
    if not employees:
        return jsonify({'message': 'No employees found'}), 404
    
    employee_list = [{
        'id': employee.id,
        'name': employee.name,
        'address_id': employee.address_id,
        'company_id': employee.company_id
    } for employee in employees]
    
    return jsonify(employee_list), 200

def get_employee(id):
    employee = Employee.query.get(id)
    
    if employee:
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'address_id': employee.address_id,
            'company_id': employee.company_id
        }), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404

def update_employee(id):
    employee = Employee.query.get(id)
    
    if employee:
        data = request.get_json()
        
        employee.name = data.get('name', employee.name)
        employee.address_id = data.get('address_id', employee.address_id)
        employee.company_id = data.get('company_id', employee.company_id)
        
        db.session.commit()
        
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'address_id': employee.address_id,
            'company_id': employee.company_id
        }), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404

def delete_employee(id):
    employee = Employee.query.get(id)
    
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': f'Employee with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404
