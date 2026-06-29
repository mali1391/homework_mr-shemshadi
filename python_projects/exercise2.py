len_word1 = len(word1)
len_word2 = len(word2)

def long_word(word1 : str, word2 : str, len_word1, len_word2):

    if len_word1 > len_word2:
        return word1
    elif len_word1 < len_word2:
        return word2
    elif len_word1 == len_word2:
        print("these words are equal")

name1 = input("enter first word: ")
name2 = input("enter second word: ")

result = long_word(name1, name2, len_word1, len_word2)

print(result)
