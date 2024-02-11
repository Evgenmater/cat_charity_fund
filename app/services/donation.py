# from datetime import datetime


# from fastapi.encoders import jsonable_encoder
# from sqlalchemy import select, false
# from sqlalchemy.ext.asyncio import AsyncSession

# from app.models import Donation, User, CharityProject


# async def investment_process(
#     user: User,
#     session: AsyncSession,
# ) -> Donation:
#     db_project = await session.execute(
#         select(CharityProject).where(
#             CharityProject.fully_invested == false()
#         )
#     )
#     data_project = db_project.scalars().first()
#     print(data_project)
#     while data_project:
#         dict_project = jsonable_encoder(data_project)
#         print(dict_project)
#         db_donations = await session.execute(
#             select(Donation).where(
#                 Donation.user_id == user.id,
#                 Donation.fully_invested == false()
#             )
#         )
#         data_donations = db_donations.scalars().first()
#         dict_donations = jsonable_encoder(data_donations)
#         print(dict_donations)
#         balance_donations = dict_donations['full_amount'] - dict_donations['invested_amount']
#         balance_project = dict_project['full_amount'] - dict_project['invested_amount']
#         print(balance_donations, balance_project)
#         if balance_donations >= balance_project:
#             print('ВЫПОЛНЯЕТСЯ КОД КОГДА ДОНАТ БОЛЬШЕ ЧЕМ В ПРОЕКТЕ')
#             result = balance_donations + dict_project['invested_amount'] - dict_project['full_amount']
#             user_invested_amount = dict_donations['full_amount'] - result + dict_donations['invested_amount']
#             setattr(data_donations, 'invested_amount', user_invested_amount)
#             setattr(data_project, 'invested_amount', dict_project['full_amount'])
#             setattr(data_project, 'fully_invested', True)
#             setattr(data_project, 'close_date', datetime.now())
#             session.add(data_project)
#             print(dict_project)
#             if dict_donations['full_amount'] == dict_donations['invested_amount']:
#                 setattr(data_donations, 'fully_invested', True)
#                 setattr(data_donations, 'close_date', datetime.now())
#                 session.add(data_donations)
#                 print('ВЫПОЛНИЛАСЬ КОМАНДА КОГДА У ЮЗЕРА ЗАКОНЧИЛСЯ ДОНАТ')
#                 break
#             print('ВЫПОЛНИЛАСЬ КОМАНДА КОГДА И У ЮЗЕРА ОСТАЛСЯ КОЛ-ВО ДОНАТА')
#             session.add(data_donations)

#         else:
#             print('ВЫПОЛНЯЕТСЯ КОД КОГДА ДОНАТА МЕНЬШЕ ЧЕМ В ПРОЕКТЕ')
#             result = balance_donations + dict_project['invested_amount']
#             user_invested_amount = dict_donations['invested_amount'] + result - dict_project['invested_amount']
#             setattr(data_donations, 'invested_amount', user_invested_amount)
#             setattr(data_project, 'invested_amount', result)
#             setattr(data_donations, 'fully_invested', True)
#             setattr(data_donations, 'close_date', datetime.now())
#             session.add(data_project)
#             session.add(data_donations)
#             break
#         db_project = await session.execute(
#             select(CharityProject).where(
#                 CharityProject.fully_invested == false()
#             )
#         )
#         data_project = db_project.scalars().first()
#     await session.commit()
#     await session.refresh(data_project)
#     return data_project

# async def investment_process(
#     user: User,
#     session: AsyncSession,
# ):
#     s = await session.get(Donation.user_id, user.id)
#     s.invested_amount = 30
#     # db_donations = await session.execute(
#     #     select(Donation).where(
#     #         Donation.user_id == user.id,
#     #         Donation.fully_invested == false()
#     #     )
#     # )
#     # db_project = await session.execute(
#     #     select(CharityProject).where(
#     #         CharityProject.fully_invested == false()
#     #     )
#     # )
#     # data_project = db_project.scalars().first()
#     # data_donations = db_donations.scalars().first()
#     # # obj_project = jsonable_encoder(data_project)
#     # obj_data = jsonable_encoder(data_donations)
#     # balance_donations = obj_data['full_amount'] - obj_data['invested_amount']
#     # setattr(data_donations, 'invested_amount', balance_donations)
#     # setattr(data_donations, 'fully_invested', True)
#     # setattr(data_donations, 'close_date', datetime.now())
#     # setattr(data_project, 'invested_amount', balance_donations)
#     # session.add(data_donations)
#     # session.add(data_project)
#     await session.commit()
