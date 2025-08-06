guess_word = ""
correct_word = "apple"
guess_cnt = 0

while guess_word != correct_word :
    if guess_cnt > 3 :
        print("out of guesses")
        break
    else:
        guess_word = input("Enter guess word: ")
        guess_cnt += 1
        if guess_word == correct_word:
            print("You win")