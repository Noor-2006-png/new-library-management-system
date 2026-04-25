from datetime import datetime, timedelta
from data import library, issued_books
from utils import get_book, get_name, get_days

def issue_book():
    book = get_book()

    if book in library and library[book]:
        name = get_name()
        days = get_days()

        return_date = datetime.now() + timedelta(days=days)

        issued_books[book] = {
            "name": name,
            "return_date": return_date
        }

        library[book] = False

        print("Book issued to", name)
        print("Return by:", return_date.date())
    else:
        print("Book not available")