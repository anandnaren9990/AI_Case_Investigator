from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import String
from src.db.base import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True
    )

    customer_risk: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    customer_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    customer_address: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )