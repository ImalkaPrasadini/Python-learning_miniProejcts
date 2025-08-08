# if letter have vowel then it replace with a


def translator(word):
    transword = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            transword = transword + "a"
        else:
            transword = transword + letter
    return transword

try:
    userInput = input('Enter word to translate: ')
    print(translator(userInput))
except ValueError as err:
    print("Invalid input", err)