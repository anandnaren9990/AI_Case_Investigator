from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Threshold(Base):
    __tablename__ = "thresholds"

    tshld_id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    aml_scenario_id: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )

    tshld_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    tshld_value: Mapped[Decimal] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )