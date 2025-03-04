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
        self.book_dao.insert_book(Book('sommaren utan regn', 'en roman', 'Maggie O farrel' ))
        self.book_dao.insert_book(Book('En oväntad vänskap', 'boken baserat på en film', 'Abdel Sellou'))
        self.book_dao.insert_book(Book('Förstå och förklara','psykologins vetenskapsteori', 'Helge malmgren'))

    def teardown_method(self):
        self.book_dao.clear_table()
        self.book_dao.close()
        self.conn.close()

    def test_get_all_books(self):
        # Verifies that 3 Books exists in database
        all_books = self.book_dao.get_all_books()
        assert len(all_books) == 3
        

    def test_add_new_book(self):
        # Verifies that a new book can be added and that its 4 total
        assert len(self.book_dao.get_all_books()) == 3
        self.book_dao.insert_book(Book("Book4","description4","author4"))
        assert len(self.book_dao.get_all_books()) == 4

    def test_get_book_by_title(self):
        # Finds a book by title and verifies that the book is correct
        temp_book = self.book_dao.find_by_title("sommaren utan regn")
        assert temp_book.description == 'en roman' 
        

    def test_get_book_and_update(self):
        # Finds a book by title and then changes description
        temp_book = self.book_dao.find_by_title("sommaren utan regn")
        temp_book.description = "sommaren med regn"
        self.book_dao.update_book(temp_book)
        updated_book = self.book_dao.find_by_title("sommaren utan regn") 
        assert updated_book.description == "sommaren med regn" 

    def test_get_book_and_delete(self):
        # Finds a book and them removes it
        temp_book = self.book_dao.find_by_title("sommaren utan regn")
        assert temp_book is not None
        self.book_dao.delete_book(temp_book)
        deleted_book = self.book_dao.find_by_title("sommaren utan regn")
        assert deleted_book == None 
        