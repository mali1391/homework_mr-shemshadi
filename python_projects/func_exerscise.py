list_of_numbers = [15685, 986, 7471, 8856]
for item in list_of_numbers:
    odd_number = lambda x: item % 2

    my_list = list(map(odd_number, list_of_numbers))
    if item:
        list_of_numbers.remove(item)
filter_list = lambda filterer: filter(list_of_numbers)
print(list_of_numbers)