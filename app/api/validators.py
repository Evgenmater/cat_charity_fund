from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject


async def check_charity_project_exists(
    charity_project_id: int,
    session: AsyncSession,
) -> CharityProject:
    """Проверка, существует ли запрашиваемый ID(переговорка)."""
    # Получаем объект из БД по ID.
    # В ответ ожидается либо None, либо объект класса CharityProject.
    # charity_project = await get_charity_project_by_id(
    #     charity_project_id, session
    # )
    # Замените вызов функции на вызов метода.
    charity_project = await charity_project_crud.get(charity_project_id, session)
    if charity_project is None:
        raise HTTPException(
            # Для отсутствующего объекта вернем статус 404 — Not found.
            status_code=404,
            detail='Благотворительный проект не найдет!'
        )
    return charity_project