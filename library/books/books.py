from flask import Blueprint
from flask import request, render_template, url_for, session

import library.adapters.repository as repo
import library.utilities.services as services

books_blueprint = Blueprint(
    'books', __name__)


@books_blueprint.route('/books_list', methods=['GET'])
def books_list():
    books_list = []
    books_Keys_list = services.book_keys_list(repo.repo_instance)


# "image_url is what the direct link to an image of the book is found; looks icon size
