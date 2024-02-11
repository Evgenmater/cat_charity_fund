
# from datetime import datetime


# open_project = {
#     'full_amount': 1500, 'fully_invested': False,
#     'create_date': '2024-02-09T14:20:56.608944',
#     'name': '2йпроект', 'invested_amount': 777, 'id': 2,
#     'close_date': None, 'description': 'для теста2'
# }
# user_donations = {
#     'id': 1, 'fully_invested': False,
#     'create_date': '2024-02-09T14:21:54.488720',
#     'user_id': 1, 'full_amount': 2332, 'invested_amount': 2000,
#     'close_date': None, 'comment': 'донатим для теста'
# }

# balance_donations = user_donations['full_amount'] - user_donations['invested_amount']
# balance_project = open_project['full_amount'] - open_project['invested_amount']
# if balance_donations >= balance_project:
#     result = balance_donations + open_project['invested_amount'] - open_project['full_amount']
#     user_donations['invested_amount'] = user_donations['full_amount'] - result + user_donations['invested_amount']
#     open_project['invested_amount'] = open_project['full_amount']
#     open_project['fully_invested'] = True
#     open_project['close_date'] = datetime.now()
#     if user_donations['full_amount'] == user_donations['invested_amount']:
#         user_donations['fully_invested'] = True
#         user_donations['close_date'] = datetime.now()
# else:
#     result = balance_donations + open_project['invested_amount']
#     user_donations['invested_amount'] = user_donations['invested_amount'] + result - open_project['invested_amount']
#     open_project['invested_amount'] = result
#     user_donations['fully_invested'] = True
#     user_donations['close_date'] = datetime.now()


# print(open_project['full_amount'], open_project['invested_amount'], open_project['fully_invested'])
# print(user_donations['full_amount'], user_donations['invested_amount'], user_donations['fully_invested'])


