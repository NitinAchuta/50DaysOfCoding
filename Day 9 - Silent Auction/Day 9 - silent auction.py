print("Welcome to the secret auction program.")

bidders = {}
more_bidders = True

while more_bidders:
    name = input('What is your name?: ')
    bid = input("What's your bid?: ")
    other_bidders = input('Are there any other bidders? y or n: ')
    bidders[name] = int(bid[1:])
    if other_bidders == 'y':
        more_bidders = True
    else:
        more_bidders = False

names = []
bids = []
top_bid = 0
top_name = ''

for key, value in bidders.items():
    names.append(key)
    bids.append(value)

for i in bids:
    if i > top_bid:
        top_bid = i
        top_name = names[bids.index(i)]

print(f'The winner is {top_name} with a bid of ${top_bid}')

