from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    description: str
    price: int
    image: str
    link: str
    
class SearchSchema(BaseModel):
    query: str

class UpdateBookRating(BaseModel):
    rating: float

class UpdateBookCopies(BaseModel):
    noOfCopies: int