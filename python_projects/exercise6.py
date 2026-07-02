def sort_list(number : int, numbers_list : list, small_numbers : tuple):
    numbers_list.sort()
    for item in numbers_list:
        if item < number:
            temp = list(small_numbers)
            temp.append(item)
            small_numbers = tuple(temp)
    return small_numbers

def check_tuple():
    duplicate_numbers = dict()
    for i in range(len(result)):
        key = result[i]
        if i == 0:
            new_value = result.count(key)
            new_item = {key : new_value}
            duplicate_numbers.update(new_item)
        elif i != 0:
            if key == result[i-1]:
                new_value = result.count(key)
                new_item = {key : new_value}
                duplicate_numbers.update(new_item)
            if key != result[i-1]:
                new_value = result.count(key)
                new_item = {key : new_value}
                duplicate_numbers.update(new_item)
    print(duplicate_numbers)

list_of_numbers = [5, 5, 64, 65, 65, 885]
small_numbers = tuple()
number = int(input("Enter your number: "))
result = sort_list(number, list_of_numbers, small_numbers)
result2 = check_tuple()
