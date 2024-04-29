library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into library.

def system(book_list):
    while True:
        title = input("What book do you want to add? ")
        author = input("Who is the author? ")
        new_book = title, author
        if new_book not in book_list:
            library.append(new_book)
        else:
            print("This book is already in the library.")
        print(library)
system(library)