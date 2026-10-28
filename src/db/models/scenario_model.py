from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Scenario(Base):
    __tablename__ = "aml_scenarios"

    aml_scenario_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
    )

    aml_scenario_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    aml_scenario_short_description: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    aml_scenario_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )