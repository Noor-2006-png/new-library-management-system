from add_book import add_book
from show_books import show_books
from issue_book import issue_book
from return_book import return_book

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")