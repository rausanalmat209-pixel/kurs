from datetime import datetime, timezone
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class UserModel(Base):
    """Model қабаты (1-әрекет): Қолданушы кестесі."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(30), default="student", nullable=False)
    total_points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    results: Mapped[list["GameResultModel"]] = relationship(back_populates="user")


class GameResultModel(Base):
    """Model қабаты (2-әрекет): Ойын нәтижелері кестесі."""

    __tablename__ = "game_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    task_name: Mapped[str] = mapped_column(String(150), nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    user: Mapped["UserModel"] = relationship(back_populates="results")

