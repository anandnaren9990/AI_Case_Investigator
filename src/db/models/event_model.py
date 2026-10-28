from datetime import datetime
from decimal import Decimal
from sqlalchemy import DateTime, String, text, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class EventGroup(Base):
    __tablename__ = "event_groups"

    event_group_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
    )

    event_group_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
    )

    alert_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    event_group_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    event_group_score: Mapped[Decimal] = mapped_column(
        Numeric(7, 2),
        nullable=False,
    )

    reason_cd: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )