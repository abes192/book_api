from flask import jsonify, request
from models.BookModel import Book
from models.CategoryModel import Category
from config import db

def get_books():
    books = Book.query.all()

    books_with_categories = []
    for book in books:
        # Ambil category terkait dari book
        category = Category.query.get(book.category_id)

        # Tambahkan detail buku beserta nama category
        books_with_categories.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'category_name': category.name if category else "No Category"
        })

    return jsonify(books_with_categories)

def get_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'status': 'error', 'message': 'Book not found'}), 404

    # Ambil category terkait dari book
    category = Category.query.get(book.category_id)

    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'category_name': category.name if category else "No Category"
    }

    return jsonify(book_data)

def add_book():
    new_book_data = request.get_json()

    new_book = Book(
        title=new_book_data['title'],
        author=new_book_data['author'],
        year=new_book_data['year'],
        category_id=new_book_data['category_id']  # Menghubungkan book dengan category
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message': 'Book added successfully!', 'book': new_book.to_dict()}), 201

# Fungsi untuk memperbarui buku (ditambahkan)
def update_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'error': 'Book not found'}), 404

    updated_data = request.get_json()
    book.title = updated_data.get('title', book.title)
    book.author = updated_data.get('author', book.author)
    book.year = updated_data.get('year', book.year)
    book.category_id = updated_data.get('category_id', book.category_id)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully!', 'book': book.to_dict()})
    
def patch_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'error': 'Book not found'}), 404

    updated_data = request.get_json()

    # Perbarui hanya jika data tersebut diberikan
    if 'title' in updated_data:
        book.title = updated_data['title']
    if 'author' in updated_data:
        book.author = updated_data['author']
    if 'year' in updated_data:
        book.year = updated_data['year']
    if 'category_id' in updated_data:
        # Pastikan Category ada sebelum meng-update
        category = Category.query.get(updated_data['category_id'])
        if category:
            book.category_id = updated_data['category_id']
        else:
            return jsonify({'error': 'Category not found'}), 404

    db.session.commit()
    return jsonify({'message': 'Book updated successfully!', 'book': book.to_dict()})

def delete_book(book_id):
    book = Book.query.get(book_id)

    if not book:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted successfully!'})
