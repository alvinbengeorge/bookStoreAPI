from pydantic import BaseModel


class BookSchema(BaseModel):
    id: str
    title: str
    author: str
    description: str
    price: int
    image: str
    link: str
    


class UpdateBookRating(BaseModel):
    rating: float

class UpdateBookCopies(BaseModel):
    noOfCopies: int