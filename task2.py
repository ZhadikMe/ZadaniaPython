# TODO Напишите функцию find_common_participants
def find_common_participant(first_group, second_group, argument=','):
    first = set(first_group.split(argument))
    second = second_group.split(argument)
    general = list(first.intersection(second))
    general.sort()
    return general



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participant(participants_first_group, participants_second_group,"|"))