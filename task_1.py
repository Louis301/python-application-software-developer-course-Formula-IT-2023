numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


numbers_without_none_element = numbers[0:4] + numbers[5:]

total = sum(numbers_without_none_element)
count = len(numbers)
average = total / count

none_element_id = 4

numbers[none_element_id] = average


print("Измененный список:", numbers)
