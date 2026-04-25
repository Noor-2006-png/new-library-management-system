from data import library
from utils import get_book

def add_book():
    book = get_book()

    if book in library:
        print("Book already exists")
    else:
        library[book] = True
        print("Book added successfully")