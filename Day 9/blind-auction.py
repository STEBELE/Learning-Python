bidders = {}

def adding_names(names,amounts):
    bidders[names] = amounts

def highest_bidder():
    highest_amount = 0
    high = 0
    winner = ""
    bids = []
    people_bidding = []
    name_highest_bidder = "" 
    for bidder in bidders:
        #1st method of determining the highest bidder
        if bidders[bidder]> highest_amount:
            high = bidders[bidder]
            winner = bidder
        #2nd method of determining the highest bidder
        bids.append(bidders[bidder])
        people_bidding.append(bidder)
    print(f"The winner is {bidder} with a bid of {high}")
    index_highest_biider = bids.index(max(bids))
    highest_amount = bids[index_highest_biider]
    name_highest_bidder = people_bidding[index_highest_biider]
    print(f"The winner is {name_highest_bidder} with a bid of {highest_amount}")
print("Welcome to the secret auction program.")
name_of_bidder = input("What is your name?: ")
bid_amount = float(input("What is your bid?: $"))
adding_names(name_of_bidder,bid_amount)


end_of_program = False
while not end_of_program:
    other_bids = input("Are there any other bidders? Type 'yes or no.'").lower()
    if other_bids =="yes":
        name_bidder = input("What is your name?: ")
        amount = float(input("What is your bid?: $"))
        adding_names(name_bidder,amount)
        end_of_program = False # dont have to change value
    elif other_bids == "no":
        highest_bidder()
        end_of_program = True

# print(bidders)
  
    
# "The winner is James with a bid of $142"

