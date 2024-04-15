from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class FighterModel(BaseModel):
    __tablename__ = "fighter"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)

    age: Mapped[int] = mapped_column(nullable=False)

    fight_art: Mapped[str] = mapped_column(nullable=False)

    fights: Mapped[int] = mapped_column(default=0)

    wins: Mapped[int] = mapped_column(default=0)
