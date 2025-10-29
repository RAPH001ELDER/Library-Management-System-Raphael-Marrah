

from operations import *

books.clear()
members.clear()

assert add_book("101", "Learn Python", "Vidal", "Fiction", 2) == "Book added successfully."
assert add_member("A01", "Tom") == "Member added successfully."
assert borrow_book("A01", "101") == "Book borrowed successfully."
assert return_book("A01", "101") == "Book returned successfully."
assert delete_book("101") == "Book deleted successfully."

print("All tests passed successfully!")
