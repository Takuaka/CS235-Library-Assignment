from flask import Blueprint
from flask import request, render_template, url_for, session

import library.adapters.repository as repo
import library.books.services as services

books_blueprint = Blueprint(
    'books_bp', __name__)


@books_blueprint.route('/books', methods=['GET'])
def books():
    book_dict = services.get_books_dict(repo.repo_instance)
    keys_list = services.get_keys_list(repo.repo_instance)
    return render_template(
        'books/books.html',
        book_dict=book_dict,
        keys_list=keys_list
    )

# "image_url is what the direct link to an image of the book is found; looks icon size
