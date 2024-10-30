from flask import Blueprint
from controllers.BookController import get_books, get_book,add_book, update_book, patch_book, delete_book

book_bp = Blueprint('book_bp', __name__)

# Route untuk mendapatkan semua buku
book_bp.route('/api/books', methods=['GET'])(get_books)

# Route untuk mendapatkan buku spesifik
book_bp.route('/api/books/<int:book_id>', methods=['GET'])(get_book)

# Route untuk menambah buku spesifik (POST)
book_bp.route('/api/books/', methods=['POST'])(add_book)

# Route untuk memperbarui buku spesifik (PATCH)
book_bp.route('/api/books/<int:book_id>', methods=['PATCH'])(update_book)

# Route untuk memperbarui buku spesifik (PUT)
book_bp.route('/api/books/<int:book_id>', methods=['PUT'])(patch_book)

# Route untuk menghapus buku spesifik (DELETE)
book_bp.route('/api/books/<int:book_id>', methods=['DELETE'])(delete_book)