############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random 
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# user_cards = [random.choice(cards),random.choice(cards)]
# computer_cards = [random.choice(cards),random.choice(cards)]
def deal_card(cards):
    """This function deals or a random card single new card from deck
    
    Args: list -- list of  cards 

    return: int(), single card
    """
    random_card = random.choice(cards)
    return random_card
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
user_cards = []
computer_cards = []
first_deal = 2
for i in range(first_deal):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

print("Welcome to blackjack!")
print(f"The users cards are ={user_cards}")
print(f" The computers cards are ={computer_cards}")
def compare_score(user_sc,computer_sc):
    if user_sc  == computer_sc:
        print("its a draw")
        return
    elif user_sc > computer_sc:
        print("You win")
        return   

    elif computer_sc > user_sc:
        print("You lose")
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(user_card,computer_card):
     total_user_score = sum(user_cards)
     total_computer_score = sum(computer_card)
     print(f" The total score for the user is = {total_user_score}")
     print(f" The total score for the computer is {total_computer_score}")
     ace = 11
     if ((total_computer_score ==21 and len(user_card)==2) or (total_user_score ==21 and len(computer_card)==2)):
         if total_computer_score ==21 and ace in computer_card:
             print("You loose, computer wins, Blackjack")
            #  end_of_game = True
         elif total_user_score ==21 and ace in user_card:
             print("Blackjack,You win")
            #  end_of_game = True
         return 0
     
     for card in computer_card:
         if card == ace and total_user_score > 21:
             computer_card.remove(card)
             computer_card.append(1)
             calculate_score(user_card,computer_card)
             print(computer_card)
     for card in user_card:
         if card ==ace and total_user_score > 21:
             user_card.remove(card)
             user_card.append(1)
             calculate_score(user_card,computer_card)
             print(user_card)
     if total_user_score > 21:
         print("Game over, You lose")
         end_of_game = True
     elif total_computer_score > 21:
         print("Game over, You win")
         end_of_game = True

     elif total_user_score <21 and total_computer_score <21:
        print('The score for both computer and player and less than 21')
        another_card = input("Do you want to get another card? Type 'y' for another one or 'n' for hold").lower()
        computer_card.append(deal_card(cards))
        if another_card == "y":
            user_card.append(deal_card(cards))
            print(user_card)
            calculate_score(user_card,computer_card)
            print(f"your new cards are {user_card}")
        elif another_card == "n":
            compare_score(total_user_score,total_computer_score)
            while total_computer_score < 17:
                print(computer_card)
                calculate_score(user_card,computer_card)

calculate_score(user_cards,computer_cards)


#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_score(cards):
    ace = 11
    if sum(cards) ==21 and len(cards)==2:
        return 0
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if ace in cards and sum(cards) > 21:
        cards.remove(ace)
        cards.append(1)
    return sum(cards)
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
is_game_over = False
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Your cards: {computer_cards}, current score: {computer_score}")
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
if user_score ==0 or computer_score ==0 or user_score >21:
    is_game_over = True
else:
    another_card = input("do you want to get another card? Type 'y' to another one, type 'n' to pass: ").lower()
    if another_card == "y":
        user_cards.append(deal_card(cards))
    else: 
        is_game_over = True
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    calculate_score = calculate_score(computer_cards)





# def adding_score(user_card,computer_card):
# user_score = 0
# computer_score =0
# for card in user_cards:
#     user_score += card
    
# for card in computer_cards:
#     computer_score += card

# print(user_score)
# print(computer_score)
# adding_score(user_card = user_cards,computer_card= computer_cards)

#checking the user score for winning numbers
#check for blackjack
# ace = 11
# if user_score ==21 or computer_score ==21:
#     if user_score ==21:
#         print("You win")
#     elif computer_score == 21:
#         print("Computer has a blackjack")
# elif user_score > 21:
#     print("the score is above 21")
# elif user_score < 21:
#     another_card = input("Do you want to get another card? ")
