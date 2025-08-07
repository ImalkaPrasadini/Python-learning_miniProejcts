# if letter have vowel then it replace with a


def translator(word):
    transword = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            transword = transword + "a"
        else:
            transword = transword + letter
    return transword

userInput = input('Enter word to translate: ')
print(translator(userInput))