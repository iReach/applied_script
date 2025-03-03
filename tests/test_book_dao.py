import book
import book_dao
import sqlite3

class TestBookDAO:
    def setup_method(self):
        #Setups the database for testing, this includes adding 3 books
        pass

    def teardown_method(self):
        # Empties database
        pass

    def test_get_all_books(self):
        # Verifies that 3 Books exists in database
        pass

    def test_add_new_book(self):
        # Verifies that a new book can be added and that its 4 total
        pass

    def test_get_book_by_title(self):
        # Finds a book by title and verifies that the book is correct
        pass

    def test_get_book_and_update(self):
        # Finds a book by title and then changes description
        pass

    def test_get_book_and_delete(self):
        # Finds a book and them removes it
        pass