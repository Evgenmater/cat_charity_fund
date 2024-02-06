# app/api/routers.py
from fastapi import APIRouter

from app.api.endpoints import (
    project_router, user_router, donation_router
)

main_router = APIRouter()
# Указываем префикс и теги для роутеров в методе include_router();
# добавляем параметры и для meeting_room_router, и для reservation_router.
main_router.include_router(
    project_router, prefix='/charity_project', tags=['Charity Project']
)
main_router.include_router(
    donation_router, prefix='/donation', tags=['Donation']
)
main_router.include_router(user_router)