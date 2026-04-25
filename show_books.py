from data import library

def show_books():
    print("\nBooks List:")
    for book, available in library.items():
        status = "Available" if available else "Issued"
        print(book, "-", status)