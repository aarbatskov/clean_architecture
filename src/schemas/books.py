from datetime import datetime
from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str
    date_birth: datetime
    biography: str


class Book(BaseModel):
    title: str
    annotation: str
    date_publishing: datetime
    author: Author
