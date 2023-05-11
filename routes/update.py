from utilities import Book, Database
from utilities import BookSchema, SearchSchema, UpdateBookCopies, UpdateBookRating
from fastapi import APIRouter, Response
from json import dumps

router = APIRouter()
db = Database()


@router.put("/rating")
def update_rating(rating: UpdateBookRating):
    id = rating.id
    book = db.get_book_by_id(id=id)
    if book:
        db.update_book(book.addRating(rating.rating), id=id)
        return Response(
            dumps({"message": "Rating updated successfully"}),
            status_code=200,
            media_type="application/json",
        )
    return Response(
        dumps({"message": "Book not found"}),
        status_code=404,
        media_type="application/json",
    )


@router.put("/copies")
def update_copies(copies: UpdateBookCopies):
    id = copies.id
    book = db.get_book_by_id(id=id)
    if book:
        db.update_book(book.changeCopies(copies.noOfCopies), id=id)
        return Response(
            dumps({"message": "Copies updated successfully"}),
            status_code=200,
            media_type="application/json",
        )
    return Response(
        dumps({"message": "Book not found"}),
        status_code=404,
        media_type="application/json",
    )
