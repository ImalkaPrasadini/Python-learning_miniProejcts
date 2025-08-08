import MCQ_Object

Q_list = [
    "Dog is a ?\n (a) Animal \n (b) Human\n\n",
    "Cat is a ?\n (a) Human \n (b) Animal\n\n",
    "Parrot is a ?\n (a) Human \n (b) Bird\n (c) Mammal\n\n"
]

QuestionWithAnswer = [
    MCQ_Object.Questions(Q_list[0], "a"),
    MCQ_Object.Questions(Q_list[1], "b"),
    MCQ_Object.Questions(Q_list[2], "b"),
]

def MCQ(QuestionWithAnswer):
    score = 0
    for Q in QuestionWithAnswer :
        answer = input(Q.Question)
        if answer ==  Q.Answer:
            score += 1
    print("You got " + str(score) +  " out of " + str(len(QuestionWithAnswer)))

MCQ(QuestionWithAnswer)