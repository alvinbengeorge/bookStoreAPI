# bookStoreAPI

This is just a simple API for a book store. It is written in Python using FastAPI

## Installation and Running
```sh
pip install -r requirements.txt
uvicorn main:app --host=0.0.0.0 --port=8000
```

## API Documentation
The API documentation is available at http://localhost:8000/docs

### `GET /books`
Returns a list of all books in the store

### `GET /books/{id}`
Returns a book with the given id

### `GET /author`
Returns all the books by the author with the given name

### `POST /search`
Searches for books with the given title and/or author
- [x] Schema
```json
{
    query: str,
}
```

### `POST /add`
Adds a new book to the store
- [x] Schema
```json
{
    title: str,
    author: str,
    description: str,
    price: int,
    image: str,
    link: str,
    availableCopies: int
}
```

### `PUT /rating`
Edits rating of the book
- [x] Schema
```json
{
    id: int,
    rating: float
}
```

### `PUT /copies`
Edits the number of copies available in the store
- [x] Schema
```json
{
    id: int,
    copies: int
}
```

### `DELETE /delete/{id}`
Deletes a book with the given id

