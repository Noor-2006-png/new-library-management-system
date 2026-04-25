from datetime import datetime
from data import library, issued_books
from utils import get_book

def return_book():
    book = get_book()

    if book in issued_books:
        record = issued_books[book]
        today = datetime.now()

        delay = (today - record["return_date"]).days
        fine = 0

        if delay > 0:
            for i in range(1, delay + 1):
                fine += 10 * i

        print("Returned by:", record["name"])
        print("Fine:", fine)

        library[book] = True
        del issued_books[book]
    else:
        print("Invalid book")