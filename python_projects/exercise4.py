def hop_game(hop_number: int, num: int):
    for i in range(num*10):
        if (i+1)%num != 0 :
            print(i+1)
        elif (i+1)%num == 0 :
            continue

    return (f"This is the hop number: {hop_number}")

num1 = int(input("Enter the hop number: "))
num2 = int(input("Enter a number: "))

result = hop_game(num1, num2)
print(result)