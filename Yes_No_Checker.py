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


# Main routine goes here ...

show_instructions = yes_no("Have you played the game before?")

print("You choose {}".format(show_instructions))
print()
Having_fun = yes_no("Are you having fun?")
print("You said {} to having fun".format(Having_fun))
