import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score:", high_score)

        print("1) Roll Dice")
        print("2) Leave Game")

        choice = input("Enter your choice:")
        if choice == "1":
            print("dice being rolled")
            roll1 = random.randint(1, 6)
            print("You rolled", roll1)
            roll2 = random.randint(1, 6)
            print("You rolled", roll2)
            score = roll1 + roll2
            print("Your total is:", score)

        if score > high_score:
            print("New high score")
            high_score = score
        elif choice == "2":
            print("Leaving game")
            exit()

        else:
            print("Please print valid answer")


dice_game()
