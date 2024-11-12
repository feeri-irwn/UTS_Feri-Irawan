from flask import Blueprint
from controllers.CompanyController import create_company, get_all_companies, get_company, update_company, delete_company

company_bp = Blueprint('company_bp', __name__)

# Route untuk mendapatkan semua perusahaan
company_bp.route('/api/companies', methods=['GET'])(get_all_companies)

# Route untuk mendapatkan perusahaan berdasarkan ID
company_bp.route('/api/company/<int:id>', methods=['GET'])(get_company)

# Route untuk menambahkan perusahaan baru
company_bp.route('/api/company', methods=['POST'])(create_company)

# Route untuk memperbarui perusahaan berdasarkan ID
company_bp.route('/api/company/<int:id>', methods=['PUT'])(update_company)

# Route untuk menghapus perusahaan berdasarkan ID
company_bp.route('/api/company/<int:id>', methods=['DELETE'])(delete_company)
