from utilities import Book, Database
from utilities import BookSchema, SearchSchema, UpdateBookCopies, UpdateBookRating
from fastapi import APIRouter, Response

router = APIRouter()
db = Database()


@router.put("/rating/{id}")
def update_rating(id: str, rating: UpdateBookRating):
    book = db.get_book_by_id(id=id)
    if book:
        db.update_book(book.addRating(rating.rating))
        return Response(
            {"message": "Rating updated successfully"},
            status_code=200,
            media_type="application/json",
        )
    return Response(
        {"message": "Book not found"}, status_code=404, media_type="application/json"
    )


@router.put("/copies/{id}")
def update_copies(id: str, copies: UpdateBookCopies):
    book = db.get_book_by_id(id=id)
    if book:
        db.update_book(book.changeCopies(copies.copies))
        return Response(
            {"message": "Copies updated successfully"},
            status_code=200,
            media_type="application/json",
        )
    return Response(
        {"message": "Book not found"}, status_code=404, media_type="application/json"
    )
