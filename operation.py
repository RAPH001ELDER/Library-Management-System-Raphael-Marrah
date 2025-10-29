

books = {}
members = {}
genres = ["Fiction", "Non-Fiction", "Sci-Fi"]


def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully."



def add_member(member_id, name):
    if member_id in members:
        return "Member already exists."
    members[member_id] = {"name": name, "borrowed_books": []}
    return "Member added successfully."



def search_book(keyword):
    results = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            results.append(f"{info['title']} by {info['author']} ({info['genre']})")
    if not results:
        return "No matching books found."
    return results



def update_book(isbn, new_title, new_author, new_genre):
    if isbn not in books:
        return "Book not found."
    if new_genre not in genres:
        return "Invalid genre."
    books[isbn]["title"] = new_title
    books[isbn]["author"] = new_author
    books[isbn]["genre"] = new_genre
    return "Book updated successfully."



def borrow_book(member_id, isbn):
    if member_id not in members:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] <= 0:
        return "No copies available."
    if isbn in members[member_id]["borrowed_books"]:
        return "Book already borrowed by member."

    books[isbn]["available_copies"] -= 1
    members[member_id]["borrowed_books"].append(isbn)
    return "Book borrowed successfully."



def return_book(member_id, isbn):
    if member_id not in members:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if isbn not in members[member_id]["borrowed_books"]:
        return "Book was not borrowed."

    books[isbn]["available_copies"] += 1
    members[member_id]["borrowed_books"].remove(isbn)
    return "Book returned successfully."

def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    del books[isbn]
    return "Book deleted successfully."
