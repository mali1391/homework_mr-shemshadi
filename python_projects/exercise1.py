def check_list(numbers : list):
    total = 0
    for num in numbers:
        total += num

    averege = total/len(numbers)
    return averege, total

list_of_numbers = [5, 6, 7]
result = check_list(list_of_numbers)

print(result)