def check_list(list1: list, set1: set):
        for x in set1:
            pass
        for i in range(len(list1)):
            if list1[i] in set1 and x in list1:
                list1.remove(list1[i])
                set1.remove(x)
                set1.update(list1)
        return set1

list1 = [52, 84, 15]
set1 = {15, 32, 44}
result = check_list(list1, set1)

print(result)