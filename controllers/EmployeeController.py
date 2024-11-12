from flask import jsonify, request
from models.EmployeeModel import Employee
from config import db

# Function to create a new employee
def create_employee():
    # Get the data from the request body (JSON format)
    data = request.get_json()
    
    # Validate the data
    if not data or not all(k in data for k in ('name', 'address_id', 'company_id')):
        return jsonify({'message': 'Name, address_id, and company_id are required fields'}), 400
    
    # Create a new Employee object using the provided data
    employee = Employee(
        name=data['name'],
        address_id=data['address_id'],
        company_id=data['company_id']
    )
    
    # Add the new employee to the session and commit it to the database
    db.session.add(employee)
    db.session.commit()
    
    # Return the created employee object as JSON
    return jsonify({
        'id': employee.id,
        'name': employee.name,
        'address_id': employee.address_id,
        'company_id': employee.company_id
    }), 201

# Function to get all employees
def get_all_employees():
    # Retrieve all employees from the database
    employees = Employee.query.all()
    
    # If no employees found, return a message
    if not employees:
        return jsonify({'message': 'No employees found'}), 404
    
    # Convert each employee to a dictionary and return as JSON
    employee_list = [{
        'id': employee.id,
        'name': employee.name,
        'address_id': employee.address_id,
        'company_id': employee.company_id
    } for employee in employees]
    
    return jsonify(employee_list), 200

# Function to get a specific employee by ID
def get_employee(id):
    # Retrieve a specific employee based on the provided ID
    employee = Employee.query.get(id)
    
    if employee:
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'address_id': employee.address_id,
            'company_id': employee.company_id
        }), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404

# Function to update an existing employee by ID
def update_employee(id):
    # Retrieve the employee object to update
    employee = Employee.query.get(id)
    
    if employee:
        # Get the data from the request body
        data = request.get_json()
        
        # Update the fields with the data provided
        employee.name = data.get('name', employee.name)
        employee.address_id = data.get('address_id', employee.address_id)
        employee.company_id = data.get('company_id', employee.company_id)
        
        # Commit the changes to the database
        db.session.commit()
        
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'address_id': employee.address_id,
            'company_id': employee.company_id
        }), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404

# Function to delete an employee by ID
def delete_employee(id):
    # Retrieve the employee to delete
    employee = Employee.query.get(id)
    
    if employee:
        # Delete the employee from the session and commit the change
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': f'Employee with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Employee with ID {id} not found'}), 404
