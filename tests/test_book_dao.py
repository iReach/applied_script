import os
import sys

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from book import Book
from book_dao import BookDAO
import sqlite3


@pytest.fixture
def book_dao():
    book_dao = BookDAO("test_book_database.db")
    book_dao.insert_book(Book('sommaren utan regn', 'en roman', 'Maggie O farrel' ))
    book_dao.insert_book(Book('En oväntad vänskap', 'boken baserat på en film', 'Abdel Sellou'))
    book_dao.insert_book(Book('Förstå och förklara','psykologins vetenskapsteori', 'Helge malmgren'))
    yield book_dao
    book_dao.clear_table()
    book_dao.close()

class TestBookDAO:
    def test_get_all_books(self, book_dao):
        # Verifies that 3 Books exists in database
        all_books = book_dao.get_all_books()
        assert len(all_books) == 3
        
    def test_add_new_book(self, book_dao):
        # Verifies that a new book can be added and that its 4 total
        assert len(book_dao.get_all_books()) == 3
        book_dao.insert_book(Book("Book4","description4","author4"))
        assert len(book_dao.get_all_books()) == 4

    def test_get_book_by_title(self, book_dao):
        # Finds a book by title and verifies that the book is correct
        temp_book = book_dao.find_by_title("sommaren utan regn")
        assert temp_book.description == 'en roman' 
        
    def test_get_book_and_update(self, book_dao):
        # Finds a book by title and then changes description
        temp_book = book_dao.find_by_title("sommaren utan regn")
        temp_book.description = "sommaren med regn"
        book_dao.update_book(temp_book)
        updated_book = book_dao.find_by_title("sommaren utan regn") 
        assert updated_book.description == "sommaren med regn" 

    def test_get_book_and_delete(self, book_dao):
        # Finds a book and them removes it
        temp_book = book_dao.find_by_title("sommaren utan regn")
        assert temp_book is not None
        book_dao.delete_book(temp_book)
        deleted_book = book_dao.find_by_title("sommaren utan regn")
        assert deleted_book == None 
        
