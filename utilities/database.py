import pymongo
import os

from dotenv import load_dotenv
from json import dumps
from typing import List

load_dotenv()


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        description: str,
        price: int,
        image: str,
        link: str,
        rating: float = 0,
        totalRatingCount: int = 1,
        availableCopies: int = 1,
        *args,
        **kwargs,
    ) -> None:
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.image = image
        self.rating = rating
        self.availableCopies = availableCopies
        self.totalRatingCount = totalRatingCount
        self.link = link
        self.id = str(kwargs.get("_id"))

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "price": self.price,
            "image": self.image,
            "link": self.link,
            "rating": self.rating,
            "totalRatingCount": self.totalRatingCount,
            "availableCopies": self.availableCopies,
            "id": self.id,
        }

    def to_json(self) -> str:
        return dumps(self.to_dict())

    def addRating(self, rating: float) -> "Book":
        self.rating = self.rating + rating / self.totalRatingCount
        self.totalRatingCount += 1
        return self

    def changeCopies(self, copies) -> "Book":
        self.availableCopies = copies
        return self

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Database:
    def __init__(self) -> None:
        self.uri = os.getenv("uri")
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client["work"]
        self.collection = self.db["books"]
        self.get_all_books()
        self.cache = []
        print("Logged in")

    def get_all_books(self) -> List[Book]:
        self.cache = [Book(**i) for i in self.collection.find()]
        return self.cache

    def search_author(self, query):
        return [Book(**i) for i in self.collection.find({"author": query})]

    def get_book_by_id(self, id):
        return Book(*self.collection.find_one({"_id": id}))

    def search_book(self, query):
        return self.collection.find({"$text": {"$search": query}})

    def local_search(self, query):
        return [
            book
            for book in self.cache
            if query in book.title.lower() or query in book.author.lower()
        ]

    def add_book(self, book: Book):
        self.collection.insert_one(book.to_dict())

    def update_book(self, book: Book):
        self.collection.update_one({"_id": book.id}, {"$set": book.to_dict()})
