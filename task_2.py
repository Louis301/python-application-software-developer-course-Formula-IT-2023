def find_common_participants(first_group, second_group, separator=','):

    first_group_list = first_group.split(separator)
    second_group_list = second_group.split(separator)

    common_participants = set(first_group_list).intersection(second_group_list)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
