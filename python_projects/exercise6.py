def calculate_mean(number : int, numbers : list, small_numbers : tuple):
    numbers.append(number)
    numbers.sort()
    if numbers[i-1] <= numbers[i-2]:
        smalls = numbers[i]
        new_list = list(small_numbers)
        new_list.append(smalls)
        small_numbers= tuple(new_list)
    elif numbers[i-1] >= numbers[i-2]:
        smalls = numbers[i-2]
        new_list = list(small_numbers)
        new_list.append(smalls)
        small_numbers= tuple(new_list)
    return number, numbers, small_numbers

def check_tuple(nums_info : dict):
    new_value = result3
    if result3 in nums_info:
        result3.count()
    key = result3
    new_item = {new_value : key}
    nums_info.update(new_item)
    return nums_info
nums_tulpe = tuple()
nums_list = []
for i in range(3):
    num = int(input("Enter your number:"))
    result1, result2, result3 = calculate_mean(num, nums_list, nums_tulpe)
print(result1 , result2)

result4 = check_tuple({})
print(result4)