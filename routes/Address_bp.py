from flask import Blueprint
from controllers.AddressController import create_address, get_all_addresses, get_address, update_address, delete_address

address_bp = Blueprint('address_bp', __name__)

# Route untuk mendapatkan semua alamat
address_bp.route('/api/addresses', methods=['GET'])(get_all_addresses)

# Route untuk mendapatkan alamat berdasarkan ID
address_bp.route('/api/address/<int:id>', methods=['GET'])(get_address)

# Route untuk menambahkan alamat baru
address_bp.route('/api/address', methods=['POST'])(create_address)

# Route untuk memperbarui alamat berdasarkan ID
address_bp.route('/api/address/<int:id>', methods=['PUT'])(update_address)

# Route untuk menghapus alamat berdasarkan ID
address_bp.route('/api/address/<int:id>', methods=['DELETE'])(delete_address)
