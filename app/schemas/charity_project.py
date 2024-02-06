from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field  # validator


class CharityProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: int = Field(..., gt=0)


class CharityProjectCreate(CharityProjectBase):
    pass


#     @validator('name')
#     # Первый параметр функции-валидатора должен называться строго cls.
#     # Вторым параметром идет проверяемое значение, его можно назвать как угодно.
#     # Декоратор @classmethod ставить нельзя, иначе валидатор не сработает.
#     def name_cant_be_numeric(cls, value: str):
#         # Если name пустой, то вываливаем ошибку:
#         if value is None:
#             # При ошибке валидации можно выбросить
#             # ValueError, TypeError или AssertionError.
#             # В нашем случае подходит ValueError.
#             # В аргумент передаём сообщение об ошибке.
#             raise TypeError('"name" является обязательным полем')
#         # Если проверка пройдена, возвращаем значение поля.
#         return value


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str]  # надо будет проверить, работают ли поля
    description: Optional[str]
    full_amount: Optional[int]


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
        extra = Extra.forbid