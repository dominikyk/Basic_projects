print("Welcome in my quiz game!")

playing = input("Do you want to play game? If so, type 'yes' ")
if playing.lower() != "yes":
    print("End of the game :( ")
    quit()
else:
    print("Okay! Let's play!")
    score = 0
print()

numbers_of_question = 4

answer1 = input("What does CPU stands for? ")
if answer1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What does GPU stands for? ")
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What does RAM stands for? ")
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("What does PSU stands for? ").lower()
if answer4 == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print()
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / numbers_of_question) * 100) + "% from the test.")

if (score / numbers_of_question) <= 0.5:
    print("You failed the test.")
else:
    print("You passed the test!")