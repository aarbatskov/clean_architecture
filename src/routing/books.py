from typing import List

from fastapi import APIRouter, Depends

from depends import get_book_service
from schemas.books import Book
from services.books import BookService

router = APIRouter(prefix="/books", tags=["books"])


@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=List[Book],
    description="Получение листинга всех книг",
)
async def get_all_books(
        book_service: BookService = Depends(get_book_service),
) -> List[Book]:
    books = book_service.get_books()
    return books


@router.post(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=Book,
    description="Создание книги",
)
async def get_all_books(
        book_service: BookService = Depends(get_book_service),
) -> Book:
    book = book_service.create_book()
    return book
