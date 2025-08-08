## Book API Endpoints

| Endpoint                | Method | Auth Required | Description                |
|-------------------------|--------|---------------|----------------------------|
| /api/books/             | GET    | No            | List all books             |
| /api/books/<id>/        | GET    | No            | Retrieve a single book     |
| /api/books/create/      | POST   | Yes           | Create a new book          |
| /api/books/<id>/update/ | PUT    | Yes           | Update book details        |
| /api/books/<id>/delete/ | DELETE | Yes           | Delete a book              |


# Filter by author name
GET /api/books/?author__name=Chinua Achebe

# Search by title or author
GET /api/books/?search=Things Fall Apart

# Order by publication year
GET /api/books/?ordering=publication_year

# Order descending
GET /api/books/?ordering=-publication_year


## API Testing Guide

This test suite ensures the API endpoints for the `Book` model function correctly.

### What’s Tested:
- List, Create, Update, Delete Book endpoints
- Search and ordering functionalities
- Authentication/permission enforcement

### How to Run:
