from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from config import session

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Customers"

    id = Column(String(36), primary_key=True, default=uuid4)
    first_name = Column(String(20))
    last_name = Column(String(20))
    tax_id = Column(String(11))
    email = Column(String(50))
    phone = Column(String(20))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def formatted_tax_id(self):
        return "{}.{}.{}-{}".format(
            self.tax_id[:3],
            self.tax_id[3:6],
            self.tax_id[6:9],
            self.tax_id[9:],
        )

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        session.add(instance)
        session.commit()
        return instance

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    def save(self):
        session.add(self)
        session.commit()

    def __repr__(self) -> str:
        return "<Customer(name='{}', email='{}')>".format(
            self.name, self.email
        )
