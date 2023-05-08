from ..utilities import Book, Database
from ..utilities import BookSchema
from fastapi import APIRouter, Response

router = APIRouter()
db = Database()

@router.get("/book/{id}")
def get_book(id: str):
    book = db.get_book(id)
    if book:
        return Response(
            book.to_json(),
            status_code=200,
            media_type="application/json"
        )
    return Response(
        "Book not found",
        status_code=404,
        media_type="application/json"
    )

@router.get("/book")
def get_all_books():
    books = db.get_all_books()
    return Response(
        BookSchema(many=True).dumps(books),
        status_code=200,
        media_type="application/json"
    )