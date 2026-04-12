list1 = [56, 786, 55320, 7486300]
list2 = [85411, 56632, 78542, 55469]
if len(list1) == len(list2):
    for i in range(len(list1)):
        lists = list()
        analogous = list(map(lambda x : x, list1))
        analog2 = list(map(lambda a : a, list2))
        lists.append(analogous[i])
        lists.append(analog2[i])
        print(lists)
else:
    pass