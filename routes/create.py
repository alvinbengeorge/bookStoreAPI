from fastapi import APIRouter, Response
from json import dumps
from utilities import Book, Database
from utilities import BookSchema

router = APIRouter()
db = Database()


@router.post("/add/")
def create_book(book: BookSchema):
    db.add_book(Book(**book.dict()))
    return Response(
        dumps({"message": "Book added successfully"}),
        status_code=200,
        media_type="application/json",
    )
