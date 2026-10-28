from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import String
from src.db.base import Base

class Case(Base):
    __tablename__ = "aml_cases"

    case_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True
    )

    focus_entity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True
    )

    event_group_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True
    )

    overall_risk: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )