from flask import Flask, render_template, Blueprint, request, redirect
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# INDEX
books_blueprint = Blueprint("books", __name__)


# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_new_book():
    #grab the form data for title, genre, publisher, author,  id
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    publisher = request.form['publisher']
    #select the author using the repository
    author = author_repository.select(author_id)
    #create a new book object
    book = Book(title, genre, publisher, author)
    #save that book object back to the database with the save method
    book_repository.save(book)

    return redirect('/books')



# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)

# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])

def delete_book(id):
    delete = book_repository.delete(id)
    return redirect('/books')
