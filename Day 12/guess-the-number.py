import random


print("Welcome to the Number Geussing Game!")
print("I'm thinking of a number between 1 and 100.")
# setting difficulty level of the game
def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    levels = {"easy": 10,"hard":5}
    num_of_attemps = 0
    if difficulty_level =="easy":
        num_of_attemps = levels["easy"]
    elif difficulty_level =="hard":
        num_of_attemps = levels["hard"]
    print(f"You have {num_of_attemps} attemps to guess the number")
    return num_of_attemps
random_number = random.randint(1,101)
# def play_again():
#     play_again = input("Do you want to play again? Type 'y' for another game and 'to end'")
#     if play_again =="y":
# num_of_attemps=set_difficulty()
# print(num_of_attemps)

def check_answer(random_number,num_of_attemps):
    end_of_game = False
    while not end_of_game:

    # def check_number(number,guess,number_of_attemps):
        if num_of_attemps ==0:
            print("You\'ve run out of guesses, you lose")
            end_of_game = True
        else:
            guess = int(input("Make a guess: "))
            if guess == random_number:
                print(f"You got it! the answer was {random_number}")
                end_of_game = True
            elif guess > random_number:
                num_of_attemps -= 1
                print("Too high")
                print("Guess again")
                print(f"You have {num_of_attemps} remaining attemps to guess the number.")
            elif guess < random_number:
                num_of_attemps -= 1
                print("Too low")
                print("Guess again")
                print(f"You have {num_of_attemps} remaining attemps to  guess the number.")

check_answer(random_number,num_of_attemps = set_difficulty())