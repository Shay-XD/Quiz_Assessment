# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no ")

def instructions():
    print("**** How to play ****")
    print()
    print("You will be asked questions related to maths")
    print()
    print("You will have to enter each question using an integer e.g a whole number")
    print()
    print(" / means divide by")
    print()
    print("Try and answer as many questions correctly as possible")
    return ""

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
print("Welcome to my maths quiz")
print()
played_before = yes_no("Have you played before")
if played_before == "no":
    instructions()



score = 0
print()
q1 = question_asker("What does 4+6 equal?", 10)
print()
q2 = question_asker("What does 9x7 equal?", 63)
print()
q3 = question_asker("What does 4x7(6-7) equal?", -28)
print()
q4 = question_asker("What does 7 to the power of 3 equal?", 343)
print()
q5 = question_asker("What does 17x32/17 equal?", 32)
print()
q6 = question_asker("What does 9 to the power of 3 equal", 729)

print("Well done your score was {} out of 6".format(score))
