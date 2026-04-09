
#
# x = list(map(lambda x: x * 2, list1))
#
# print(x)
i = 0
list1 = [15685, 986, 7471, 8856]
for item in list1:
    odd = lambda x: item % 2

    my_list = list(map(odd, list1))
    if item:
        list1.remove(item)
    else:
        pass
filter_list = lambda filter: filter(list1)
print(list1)