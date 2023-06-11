# List to store information about books
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "available"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "available"},
    {"id": 3, "title": "1984", "author": "George Orwell", "status": "borrowed"},
    # Add more books here...
]

# List to store information about students
students = [
    {"id": 1, "name": "John Doe", "books_borrowed": [1, 2]},
    {"id": 2, "name": "Jane Smith", "books_borrowed": [3]},
    # Add more students here...
]

# List to store information about transactions
transactions = [
    {"book_id": 1, "student_id": 1, "due_date": "2023-06-20"},
    {"book_id": 2, "student_id": 1, "due_date": "2023-06-15"},
    {"book_id": 3, "student_id": 2, "due_date": "2023-06-18"},
    # Add more transactions here...
]
