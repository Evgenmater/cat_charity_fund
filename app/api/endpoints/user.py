from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, User, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(User, UserCreate),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(User, UserUpdate),
    prefix='/users',
    tags=['users'],
)


@router.delete(
    '/users/{id}',
    tags=['users'],
    deprecated=True
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        # 405 ошибка - метод не разрешен.
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )