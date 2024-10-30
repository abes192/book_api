from flask import Blueprint
from controllers.CategoryController import get_categories,add_category, get_category, update_category, delete_category

category_bp = Blueprint('Category_bp', __name__)

# Route untuk mendapatkan semua kategori
category_bp.route('/api/category', methods=['GET'])(get_categories)

# Route untuk menambahkan semua kategori
category_bp.route('/api/category', methods=['POST'])(add_category)

# Route untuk mendapatkan kategori spesifik
category_bp.route('/api/category/<int:cat_id>', methods=['GET'])(get_category)

# Route untuk memperbarui kategori spesifik (PUT)
category_bp.route('/api/category/<int:cat_id>', methods=['PUT'])(update_category)

# Route untuk menghapus kategori spesifik (DELETE)
category_bp.route('/api/api/category/<int:cat_id>', methods=['DELETE'])(delete_category)