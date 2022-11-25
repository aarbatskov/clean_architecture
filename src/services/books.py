from typing import List

from repositories.books import BookRepository
from schemas.books import Book


class BookService:

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def get_books(self) -> List[Book]:
        result = self.repository.get_books()
        return result

    def create_book(self) -> Book:
        result = self.repository.create_book()
        return result