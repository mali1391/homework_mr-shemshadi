def hop_game(hop_number: int, number_of_numbers: int):
    for i in range(hop_number*10):
        if (i+1)%number_of_numbers != 0 :
            print(i+1)
        elif (i+1)%number_of_numbers == 0 :
            continue

    return (f"This is the hop number: {hop_number}")

hop_number = int(input("Enter the hop number: "))
number_of_numbers = int(input("Enter numebr of numbers: "))

result = hop_game(hop_number, number_of_numbers)
print(result)
