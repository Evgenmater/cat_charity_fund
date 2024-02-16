from datetime import datetime
from typing import Union

from sqlalchemy import select, false
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Donation, CharityProject


async def get_open_object(
        db_obj: Union[CharityProject, Donation],
        session: AsyncSession
) -> list[Union[CharityProject, Donation]]:
    """Функция для поиска в БД все открытые проекты."""
    db_obj_in = await session.execute(
        select(db_obj).where(
            db_obj.fully_invested == false()
        ).order_by('create_date')
    )
    return db_obj_in.scalars().all()


async def investment_process(
    db_obj: Union[CharityProject, Donation],
    obj_in: Union[CharityProject, Donation],
    session: AsyncSession,
):
    """Функция для процесса инвестирования."""
    obj_data = await get_open_object(db_obj, session)
    for field in obj_data:
        money_donation = obj_in.full_amount - obj_in.invested_amount
        adding_funds = field.invested_amount + money_donation
        if adding_funds > field.full_amount:
            obj_in.invested_amount = field.full_amount - field.invested_amount + obj_in.invested_amount
            field.invested_amount = field.full_amount
            field.fully_invested = True
            field.close_date = datetime.now()
        elif adding_funds == field.full_amount:
            field.invested_amount = field.full_amount
            obj_in.invested_amount = obj_in.full_amount
            field.fully_invested = True
            field.close_date = datetime.now()
            obj_in.fully_invested = True
            obj_in.close_date = datetime.now()
            break
        else:
            field.invested_amount = adding_funds
            obj_in.invested_amount = obj_in.full_amount
            obj_in.fully_invested = True
            obj_in.close_date = datetime.now()
        session.add(field)
        session.add(obj_in)
    await session.commit()
    await session.refresh(obj_in)
