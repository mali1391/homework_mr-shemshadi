def fat_students_in_school(students: dict, fat_students: list, name: str, weight: int):
    info = {name : weight}
    students.update(info)

    if weight > 70:
        fat_students.append(name)


    elif weight <= 70:
        print("This student isn't fat!")

    return fat_students
def sort_list(fat_students : list):
    result.sort()
    return result

students_list = dict()
list_of_fat_students = list()
sort_of_fat_students_list = list()
for i in range(2):
    student_name = input("Enter student name: ")
    student_weight = int(input("Enter student weight: "))

    result = students_info(students_list, list_of_fat_students, student_name, student_weight)

print(f"This is the list of fats: {result}")

result2 = sort_list(sort_of_fat_students_list)
print(f"This is the sort list of fats: {result2}")