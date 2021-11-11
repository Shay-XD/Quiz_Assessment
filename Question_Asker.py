# Functions go here
def question_asker(question, answer):
    error = "please enter a number"
    global score
    while True:
        try:
            response = int(input(question))
            if response == answer:
                score += 1
                print("correct")
            else:
                print("incorrect")
            return response
        except ValueError:
            print(error)


# Main routine


score = 0

q1 = question_asker("What does 4+6 equal?", 10)
q2 = question_asker("What does 9x7 equal?", 63)
q3 = question_asker("What does 4x7(6-7) equal?", -28)
q4 = question_asker("What does 7 to the power of 3 equal?", 343)
q5 = question_asker("What does 17x32/17 equal?", 32)
q6 = question_asker("What does 9 to the power of 3 equal", 729)

print(score)
print("Well done your score was {} out of 6".format(score))
