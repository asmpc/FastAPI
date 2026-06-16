from datetime import datetime
from typing import Optional, Annotated
from sqlalchemy import String, text
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    DeclarativeBase,
)


primary_integer = Annotated[int, mapped_column(primary_key=True, auto_increment=True)]
string_64_nullable = Annotated[str, mapped_column(String(64), nullable=True)]
string_64_not_nullable = Annotated[str, mapped_column(String(64))]
string_64_unique = Annotated[str, mapped_column(String(64), unique=True)]

simple_integer_nullable = Annotated[Optional[int], mapped_column(nullable=True)]

created_at = Annotated[
    datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]

updated_at = Annotated[
    datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]


class Base(DeclarativeBase):
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

