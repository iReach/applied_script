import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from book import Book
from book_dao import BookDAO
import sqlite3

class TestBookDAO:
    def setup_method(self):
        #Setups the database for testing, this includes adding 3 books
        self.conn = sqlite3.connect('test_book_database.db')
        self.cursor = self.conn.cursor()
        self.book_dao = BookDAO("test_book_database.db")
        self.book_dao.insert_book(Book("Book1", "description1", "author1"))
        self.book_dao.insert_book(Book("Book2", "description2", "author2"))
        self.book_dao.insert_book(Book("Book3", "description3", "author3"))

    def teardown_method(self):
        self.book_dao.clear_table()
        self.book_dao.close()
        self.conn.close()

    def test_get_all_books(self):
        # Verifies that 3 Books exists in database
        pass

    def test_add_new_book(self):
        # Verifies that a new book can be added and that its 4 total
        assert len(self.book_dao.get_all_books()) == 3
        self.book_dao.insert_book(Book("Book4","description4","author4"))
        assert len(self.book_dao.get_all_books()) == 4

    def test_get_book_by_title(self):
        # Finds a book by title and verifies that the book is correct
        pass

    def test_get_book_and_update(self):
        # Finds a book by title and then changes description
        pass

    def test_get_book_and_delete(self):
        # Finds a book and them removes it
        pass