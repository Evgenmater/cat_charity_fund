# from typing import Optional

# # from fastapi.encoders import jsonable_encoder
from datetime import datetime
from fastapi.encoders import jsonable_encoder
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
        Возвращать список объектов Donation,
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

    async def create_donation(
        self,
        new_donation: DonationCreate,
        user: User,
        session: AsyncSession,
    ) -> Donation:
        new_donation_data = new_donation.dict()
        new_donation_data.update(create_date=datetime.now(), user_id=user.id)
        db_donation = Donation(**new_donation_data)
        session.add(db_donation)
        await session.commit()
        await session.refresh(db_donation)

        return db_donation


donation_crud = CRUDDonation(Donation)