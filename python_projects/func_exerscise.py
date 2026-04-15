list1 = [15685, 986, 7471, 8856]
for item in list1:
    odd_number = lambda x: item % 2

    my_list = list(map(odd_number, list1))
    if item:
        list1.remove(item)
filter_list = lambda filterer: filter(list1)
print(list1)
