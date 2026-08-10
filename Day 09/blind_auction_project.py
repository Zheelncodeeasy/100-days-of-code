import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

#printing logo
print(art.logo)

# Creating empty dictionary for bidders
bidders = {}

# flag to stop the loop
more_bidders = True

# loop will break when more_bidders becomes False
while more_bidders:
    # Take inputs
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What is your bid?: $"))

    # saving data to bidders dictionary
    bidders[bidder_name] = bidder_amount

    # check if there are more bidders
    any_other_bidders = input("Are there any other bidders? Type 'yes or 'no'.: ").lower()

    # max bidder name
    max_bid_name = ""

    # max value for a bid
    max_bid_amount = 0

    # loop through bidders to find the highest bidders
    for key, val in bidders.items():
        if val > max_bid_amount:
            max_bid_name = key
            max_bid_amount = val

    # if there are more bidders
    if any_other_bidders == "yes":
        print("\n" * 20)
        more_bidders = True
    else:
        more_bidders = False
        print(f"The winner is {max_bid_name} with a bid of ${max_bid_amount}")






