from flask import Blueprint
from controllers.EmployeeController import create_employee, get_all_employees, get_employee, update_employee, delete_employee

employee_bp = Blueprint('employee_bp', __name__)

employee_bp.route('/api/employees', methods=['GET'])(get_all_employees)

employee_bp.route('/api/employee/<int:id>', methods=['GET'])(get_employee)

employee_bp.route('/api/employee', methods=['POST'])(create_employee)

employee_bp.route('/api/employee/<int:id>', methods=['PUT'])(update_employee)

employee_bp.route('/api/employee/<int:id>', methods=['DELETE'])(delete_employee)
