def check_list(list1 : list, list2 : list):
    for i in range (len(list1)):
        if list1[i] in list2:
            if list1[i] == list2[i]:
                list1.remove(list1[i])
                list2.remove(list2[i])
            elif list1[i] != list2[i]:
                list1.remove(list1[i])
            return list1, list2
        if list2[i] in list1:
            if list2[i] == list1[i]:
                list1.remove(list1[i])
                list2.remove(list2[i])
            elif list2[i] != list1[i]:
                list2.remove(list2[i])
            return list1, list2

list1 = [52, 84, 15]
list2 = [15, 32, 85]
result = check_list(list1, list2)

print(result)