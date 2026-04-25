def get_book():
    return input("Enter book name: ").lower()

def get_name():
    return input("Enter student name: ")

def get_days():
    try:
        return int(input("Enter number of days: "))
    except:
        return 1