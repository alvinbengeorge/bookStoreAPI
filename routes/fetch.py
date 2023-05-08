from ..utilities import Book, Database
from ..utilities import BookSchema
from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/{id}")
def get_book(id: str):
    book = Database().get_book(id)
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