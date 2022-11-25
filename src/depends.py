from repositories.books import BookRepository
from services.books import  BookService

"""
Файл внедрения зависимостей
"""

# repository - работа с БД

book_repository = BookRepository()

# service - слой UseCase

book_service = BookService(book_repository)


def get_book_service() -> BookService:
    return book_service
