from sqlalchemy import Column, String, Text

from app.core.db import Base
from .base import ProjectAndDonationBase


class CharityProject(ProjectAndDonationBase, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
