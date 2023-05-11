from utilities import Book, Database
from utilities import BookSchema, SearchSchema
from fastapi import APIRouter, Response
from json import dumps

router = APIRouter()
db = Database()


@router.get("/book/{id}")
def get_book(id: str):
    book = db.get_book_by_id(id)
    if book:
        return Response(
            dumps(book.to_json(id=id)), status_code=200, media_type="application/json"
        )
    return Response(
        dumps({"message": "Book not found"}), status_code=404, media_type="application/json"
    )


@router.get("/book")
def get_all_books():
    books = db.get_all_books()
    return Response(
        dumps([book.to_dict(book.kwargs.get("_id")) for book in books]),
        status_code=200,
        media_type="application/json",
    )


@router.post("/search")
async def search(search: SearchSchema):
    result = db.search_book(search.query.lower())
    return Response(dumps(result), status_code=200, media_type="application/json")


@router.post("/cache-search")
async def search_cache(query: str):
    result = db.local_search(query.lower())
    return Response(
        dumps([book.to_dict() for book in result]),
        status_code=200,
        media_type="application/json",
    )


@router.get("/author")
async def search_author(query: str):
    result = db.search_author(query.lower())
    return Response(
        dumps([book.to_dict(book.kwargs.get("_id")) for book in result]),
        status_code=200,
        media_type="application/json",
    )
