def check_list(list1: list, set1: set):
    for x in range(len(set1)):
        for i in range(len(list1)):
            if list1[i] in set1:
                if list1[i] == set1:
                    list1.remove(list1[i])
                    del (set1)
                elif list1[i] != set1:
                    list1.remove(list1[i])
                return list1, set1
            if set1 in list1:
                if set1 == list1[i]:
                    list1.remove(list1[i])
                    del (set1)
                elif set1[x] != list1[i]:
                    del (set1)
                return list1, set1

list1 = [52, 84, 15]
set1 = {15, 32, 85}
result = check_list(list1, set1)

print(result)