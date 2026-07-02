def long_word(word1 : str, word2 : str, len_word1: int, len_word2: int):

    if len_word1 > len_word2:
        return word1
    elif len_word1 < len_word2:
        return word2
    elif len_word1 == len_word2:
        print("these words are equal")

name1 = input("enter first word: ")
name2 = input("enter second word: ")
len_name1 = len(name1)
len_name2 = len(name2)
result = long_word(name1, name2, len_name1, len_name2)

print(result)
