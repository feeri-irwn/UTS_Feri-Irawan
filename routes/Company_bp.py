from flask import Blueprint
from controllers.CompanyController import create_company, get_all_companies, get_company, update_company, delete_company

company_bp = Blueprint('company_bp', __name__)

company_bp.route('/api/companies', methods=['GET'])(get_all_companies)

company_bp.route('/api/company/<int:id>', methods=['GET'])(get_company)

company_bp.route('/api/company', methods=['POST'])(create_company)

company_bp.route('/api/company/<int:id>', methods=['PUT'])(update_company)

company_bp.route('/api/company/<int:id>', methods=['DELETE'])(delete_company)
