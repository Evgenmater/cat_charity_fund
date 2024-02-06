# from typing import Optional

# # from fastapi.encoders import jsonable_encoder
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User
from app.schemas.donation import DonationCreate


class CRUDDonation(CRUDBase):

    async def get_my_donations(
        self,
        user: User,
        session: AsyncSession,
    ) -> list[Donation]:
        """
        Возвращать список объектов Reservation,
        связанных с пользователем, выполняющим запрос
        """
        user_donations = await session.execute(
            # Получить все объекты Donation.
            select(Donation).where(
                # Где внешний ключ Donation.user_id
                # равен user.id пользователя.
                Donation.user_id == user.id
            )
        )
        user_donations = user_donations.scalars().all()
        return user_donations

    async def create_him(
        self,
        new_project: DonationCreate,
        session: AsyncSession,
    ) -> Donation:
        new_project_data = new_project.dict()
        new_project_data['create_date'] = datetime.now()
        db_room = Donation(**new_project_data)
        session.add(db_room)
        await session.commit()
        await session.refresh(db_room)
        return db_room


donation_crud = CRUDDonation(Donation)