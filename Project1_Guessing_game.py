# This project is about the casino game where I have used random function to generate random numbers by the computer
# which the player will have to guess. There is individual prize allocated for the desired package.


import random


def greet(fx):
    def mfx(*args, **kwargs):
        print(
            "Hi, welcome to the Royal Casino! Try your luck here. Check out our packages and select one. Remember the "
            "prize- \nif you guess in 2 chance, you will win 20 million.\nIf you guess in 3 chances, you will win "
            "20000.\nIf you guess in 5 chances, you will win 2000. Give a try to your luck.")
        fx(*args, **kwargs)
        print("Good luck to you. Remember, this is not the end of the world.")

    return mfx


print("1. press 'y' to continue the game.\n2. press 'n' or any character to quit the game.")
press = input("")

if press == "y":
    @greet
    def start(f):
        print(
            "You have entered in the game. Once you entered, please read the instructions very carefully. \nThere is "
            "no going back from here. Choose you number wisely otherwise wrong numbers might make you to lose your "
            "money \nSelect any of the packages:\n 2. 2 guess and win 20 million(cost you £200)\n 3. 3 guess and win "
            "20000(cost you £300)\n 5. 5 guess and win 2000(cost you £399). "
        )
        choice = int(input())
        if choice == 2:
            def guess(x):
                random_num = random.randint(1, x)

                z = input("To confirm press 'y' again.")
                while z != "n":
                    c = 2
                    while c > 0:
                        guess1 = int(input(f"Guess a number between 1 to {x}: "))
                        if guess1 > random_num:
                            print("Sorry dude, guess again. Too High")
                        elif guess1 < random_num:
                            print("Sorry, guess again. Too Low")
                        elif guess1 == random_num:
                            print("Congrats, You have made it!!\nYou have won £20 million")
                            break

                        c -= 1
                    break

            guess(10)
        if choice == 3:
            def guess(x):
                random_num = random.randint(1, x)
                z = input("To confirm press 'y' again.")
                while z != "n":
                    c = 3
                    while c > 0:
                        guess1 = int(input(f"Guess a number between 1 to {x}: "))
                        if guess1 > random_num:
                            print("Sorry dude, guess again. Too High")
                        elif guess1 < random_num:
                            print("Sorry, guess again. Too Low")
                        elif guess1 == random_num:
                            print("Congrats, You have made it!!\nYou have won £20000")
                            break

                        c -= 1
                    break

            guess(15)
        if choice == 5:
            def guess(x):
                random_num = random.randint(1, x)
                z = input("To confirm press 'y' again.")
                while z == "y":
                    c = 5
                    while c > 0:
                        guess1 = int(input(f"Guess a number between 1 to {x}: "))
                        if guess1 > random_num:
                            print("Sorry dude, guess again. Too High")
                        elif guess1 < random_num:
                            print("Sorry, guess again. Too Low")
                        elif guess1 == random_num:
                            print("Congrats, You have made it!!\nYou have won £2000")
                            break

                        c -= 1
                    break

            guess(25)


    start(1)
elif press == "n":
    print("This is not the end. Try you luck here. Who knows, you might be a millionaire!!")

############### Random Practices
"""
print("A random number between 0 and 1 is: ", end="")
print(random.random())
print("A random number from range is: ", end="")

print(random.randrange(20,50,3))"""

"""for i in range(5):
    random.seed(0)
    print(random.randint(1, 1000))"""
