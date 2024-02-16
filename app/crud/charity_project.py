from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_charity_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Метод для поиска в БД переданного имени."""
        db_project_name_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_name_id.scalars().first()

    async def get_project_id_by_full_amount(
        self,
        project_full_amount: int,
        session: AsyncSession,
    ) -> Optional[int]:
        """
        Метод для поиска в БД внесённой суммы, которая больше требуемой суммы.
        """
        db_project_full_amount_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.invested_amount > project_full_amount
            )
        )
        return db_project_full_amount_id.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)