# from typing import Optional
from datetime import datetime
# # from fastapi.encoders import jsonable_encoder
# from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate


# Создаем новый класс, унаследованный от CRUDBase. В нём описаны методы,
# которые аналогичные ниже закомментированным функциям, кроме одного метода.
class CRUDCharityProject(CRUDBase):

    async def create_project(
        self,
        new_project: CharityProjectCreate,
        session: AsyncSession,
    ) -> CharityProject:
        new_project_data = new_project.dict()
        new_project_data['create_date'] = datetime.now()
        db_project = CharityProject(**new_project_data)
        session.add(db_project)
        await session.commit()
        await session.refresh(db_project)
        return db_project


# Объект crud наследуем уже не от CRUDBase,
# а от только что созданного класса CRUDCharityProject, для использования доп.
# метода. Для инициализации передаем модель, как и в CRUDBase.
charity_project_crud = CRUDCharityProject(CharityProject)