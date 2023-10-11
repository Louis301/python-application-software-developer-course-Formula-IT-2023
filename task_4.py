users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

user_visits = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}

user_visits["Общее количество"] = len(users)
user_visits["Уникальные посещения"] = len(set(users))

print(user_visits)

