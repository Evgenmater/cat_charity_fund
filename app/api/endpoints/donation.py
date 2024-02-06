from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.db import get_async_session
# from app.core.user import current_superuser
from app.crud.donation import donation_crud
from app.schemas.donation import (
    DonationAdminDB, DonationCreate, DonationDB
)
from app.core.user import current_user
from app.models import User

router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
)
async def create_donation(
    charity_project: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Сделать пожертвование."""
    create_new_project = await donation_crud.create_him(
        obj_in=charity_project, session=session
    )
    # Создаём пожертвоние,
    # далее нужен метод, в котором будет:
    # 1) Проверять на наличие открытых проектов fully_invested
    # 2) Если нету открытых проектов, то
    #    - оставляем сумму до открытия следующего проекта
    # 3) Если есть открытые проекты, то берём первый открытый проект(по времени или по id)
    #    - Проверяем какую сумму нужно до закрытия проекта
    #       а) если у пользователя больше или равно суммы для закрытия, то добавляем нужную сумму(вычитаем у пользователя сумму),
    #          закрываем проект и если сумма остается, то добавляем в следующий открытый проект,
    #       б) если следующего проекта нету, то оставляем сумму у в фонде(у пользователя)
    return create_new_project


@router.get(
    '/',
    response_model=list[DonationAdminDB],
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.\n
    Получает список всех пожертвований.
    """
    all_charity_project = await donation_crud.get_multi(session=session)
    return all_charity_project


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Получить список моих пожертвований."""
    my_donations = await donation_crud.get_my_donations(
        user=user, session=session
    )
    return my_donations