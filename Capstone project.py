import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
        def start_game():
            random_number = int(random.randint(1,10))
            print("Hey There! Welcome to the game of guesses!")
            player_name = input("Enter your name!")
            wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No ".format(player_name))
            ## where the show_score function USED to be attempts = 0
            show_score()
            while wanna_play.lower() == "yes":
                try:
                    guess = input("Pick a number between 1 and 10 ")
                    if int(guess) < 1 or int(guess) > 10:
                        raise ValueError("Please guess a number within the given range")
                    if int(guess) == random_number:
                        print("Congrats! you got it right!")
                        attempts += 1
                        attempts_list.append(attempts)
                        print("It took you {} attempts".format(attempts))
                        play_again = input("Would you like to play again?" (enter Yes/No))


                        attempts = 0
                        show_score()
                        random_number = int(random.randit(1,10))
                        if play_again.lower() == "no":
                            print("That's cool, sooooooo have a nice day pal!")
                            break
                        elif int(guess) < random_number:
                            print("It's lower")
                            attempts += 1
                        elif int(guess) > random_number:
                            print("Its Higher")
                            attempts += 1
                        except ValueError as err:
                            print("Oops!,that is not a valide value. Try again...")
                            print("({})".format(err))
                    else:
                        print("That's cool, have a nice day!")
                        if __name__ == '__main__':
                            start_game()