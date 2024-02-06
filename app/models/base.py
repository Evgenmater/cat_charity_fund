from sqlalchemy import Column, Integer, Boolean, DateTime

from app.core.db import Base


class ProjectAndDonationBase(Base):
    __abstract__ = True
    full_amount = Column(Integer)
    fully_invested = Column(Boolean, default=False)
    invested_amount = Column(Integer, default=0)
    create_date = Column(DateTime)
    close_date = Column(DateTime)
