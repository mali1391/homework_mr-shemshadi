def mergeSort(arr : list, message : str):
  if len(arr) <= 1:
    return arr

  if message == "up":
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf, message)
    sortedRight = mergeSort(rightHalf, message)
    return merge(sortedLeft, sortedRight)

  elif message == "down":
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort(leftHalf, message)
    sortedRight = mergeSort(rightHalf, message)
    return merge2(sortedLeft, sortedRight)

  else:
    print("error")
    return False
def merge(left, right):
  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result

def merge2(left, right):
  result2 = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      result2.append(left[i])
      i += 1
    else:
      result2.append(right[j])
      j += 1
  result2.extend(left[i:])
  result2.extend(right[j:])
  return result2

my_list = [3, 7, 6, -10, 15, 23.5, 55, -13]
txt_message = input("Enter your message: ")
my_sortedlist = mergeSort(my_list, txt_message)
print("Sorted array:", my_sortedlist)