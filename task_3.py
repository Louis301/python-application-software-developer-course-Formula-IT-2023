list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

count_players = len(list_players)

list_players_half_id = count_players // 2

first_team = list_players[:list_players_half_id]
second_team = list_players[list_players_half_id:]

print(first_team)
print(second_team)
