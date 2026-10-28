from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import String, JSON
from src.db.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    alert_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
    )

    focus_entity: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    aml_scenario_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    highlights: Mapped[dict[str,any]] = mapped_column(
        JSON,
        nullable=False
    )