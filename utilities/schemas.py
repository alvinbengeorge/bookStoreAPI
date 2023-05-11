from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    description: str
    price: int
    image: str
    link: str
    availableCopies: int


class SearchSchema(BaseModel):
    query: str


class UpdateBookRating(BaseModel):
    id: str
    rating: float


class UpdateBookCopies(BaseModel):
    id: str
    noOfCopies: int
