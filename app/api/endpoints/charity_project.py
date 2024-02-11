from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.validators import check_charity_project_exists

from app.core.db import get_async_session
# from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectDB, CharityProjectUpdate
)

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.\n
    Создает благотворительный проект.
    """
    create_new_project = await charity_project_crud.create_project(
        new_project=charity_project, session=session
    )
    # Создаём метод, который будет проверять при открытии нового проекта, есть ли пожертвование в фонде
    # - если пожертвования есть, то проверяем какую сумму нужно до закрытия проекта
    #       а) если у пожертвования больше или равно суммы для закрытия, то добавляем нужную сумму(вычитаем у пользователя сумму)
    #          закрываем проект и если сумма остается, то добавляем в следующий открытый проект,
    #       б) если следующего проекта нету, то оставляем сумму у в фонде(у пользователя)
    return create_new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_project(
    session: AsyncSession = Depends(get_async_session),
):
    """Получает список всех проектов."""
    all_charity_project = await charity_project_crud.get_multi(session=session)
    return all_charity_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    charity_project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.\n
    Закрытый проект нельзя редактировать,
    также нельзя установить требуемую сумму меньше уже вложенной.
    """
    charity_project = await check_charity_project_exists(
        charity_project_id=charity_project_id, session=session
    )

    # if obj_in.name is not None:
    #     # Если в запросе получено поле name — проверяем его на уникальность.
    #     await check_name_duplicate(obj_in.name, session)

    # Заменим вызов функции на вызов метода.
    charity_project = await charity_project_crud.update(
        db_obj=charity_project, obj_in=obj_in, session=session
    )
    return charity_project


@router.delete(
    '/{meeting_room_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.\n
    Удаляет проект. Нельзя удалить проект,
    в который уже были инвестированы средства, его можно только закрыть.
    """
    charity_project = await check_charity_project_exists(
        charity_project_id=charity_project_id, session=session
    )
    charity_project = await charity_project_crud.remove(
        db_obj=charity_project, session=session
    )
    return charity_project