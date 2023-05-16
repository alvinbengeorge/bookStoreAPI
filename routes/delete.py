from fastapi import APIRouter, Response
from json import dumps
from utilities import Book, Database

router = APIRouter()
db = Database()


@router.delete("/delete/{id}")
def delete_book(id: str):
    book: Book = db.get_book_by_id(id=id)
    if book:
        db.delete_book(id=id)
        return Response(
            dumps({"message": "Book deleted successfully", "data": book.to_dict()}),
            status_code=200,
            media_type="application/json",
        )
    return Response(
        dumps({"message": "Book not found"}),
        status_code=404,
        media_type="application/json",
    )
