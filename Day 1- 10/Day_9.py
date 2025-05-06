# Bid 
import os

print("Welcome to the Secret auction program")

bids = {}
bidding_finished = False
def fined_hiest(bid_recorde):
    highst_bid = 0
    for bidding in bid_recorde:
        bid_amount = bid_recorde[bidding]
        if bid_amount > highst_bid:
            highst_bid = bid_amount
            winner = bidding
            print(f"The winner is {winner} with a bid of ${highst_bid}")
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if should_continue == ["no","n","N"]:
        bidding_finished = True
        fined_hiest(bids)
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')

# You can add code here to determine the highest bidder and print the result