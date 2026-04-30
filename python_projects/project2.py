def bubble_merge(my_list : list, message : str):
  length = len(mylist)
  for i in range(length - 1):
    for j in range(length - i - 1):
      if mylist[j] > mylist[j + 1]:
        mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
      return my_list

  mylist = [64, 34, 25, 12, 22, 11, 90, 5]
  txt_message = input("Enter your message: ")
  result = bubble_merge(mylist, message)
  print(result)