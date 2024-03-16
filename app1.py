# Auction

# Instructions and rules of the Auction
print (""" 
Welcome to the Mega Auction House!
The below shown are the Rules and Regulations of the Auction
    1. The bid starts with the minimun bid amount
    2. Participants can bid with higher amount if they wish
    3. Bid the amount by saying your Name
    4. The Auction ends when no more bids are made
    5. The highest Bidder wins the Auction
"""
)

# input of the product name and the starting price
product_name = input("Enter the Product Name : ")
starting_price = float(input("Enter the starting price of the product : "))

# create dictionary to store bid
bids = {}

# initial bid
bidder = input("Enter your Name : ")
bid_amount = float(input("Enter your Bid amount : "))
bids[bidder] = bid_amount

# Bidding process in loop mode
while True:
    continue_bidding = input("Does anyone want to bid more ? (yes/no): ")
    if continue_bidding.lower() == "yes":
        bidder = input("Enter your Name : ")
        bid_amount = float(input("Enter your Bid amount : "))
        bids[bidder] = bid_amount
    elif continue_bidding.lower() == "no":
        break
    else:
        print("Invalid input, Please enter 'yes' or 'no'")

# find the winner
winning_bidder = max(bids, key = bids.get)
winning_bid = bids[winning_bidder]

#Auction Result
print(f"""
Auction Result 
Product {product_name}
Starting price {starting_price}
Winner of the Auction {winning_bidder}
The Amount he/she bid {winning_bid}
"""
      )