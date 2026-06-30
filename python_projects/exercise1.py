def average_func(numbers : list):
    total = 0
    for num in numbers:
        total += num
    average = total/len(numbers)
    return average, total

list_of_numbers = [5, 6, 7]
result = average_func(list_of_numbers)

print(result)