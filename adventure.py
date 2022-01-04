name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you choose? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across. Type walk to walk and swim to swim across ").lower()

    if answer == "swim":
        print("You swam across the river and were eaten by alligator. You died")
    elif answer == "walk":
        print("You had walked for many miles and ran out of water. You lost the game ")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a  bridge. Do you want to cross it? ")

else:
    print("Not a valid option. You lose.")