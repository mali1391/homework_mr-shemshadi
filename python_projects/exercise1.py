total = 0
def average_func(numbers : list, total):
    for num in numbers:
        total += num
    average = total/len(numbers)
    return average, total

list_of_numbers = [5, 6, 7]
result = average_func(list_of_numbers)

print(result)
