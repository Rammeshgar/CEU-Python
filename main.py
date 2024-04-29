from replit import clear

bids={}
new_bids="yes"
while new_bids=="yes":
  name=input("Whats your name? ")
  money=float(input("enter your money? $"))
  bids[name]=money
  new_bids=input("new bids? yes or no ")
  clear()
print(bids)

biggest_bid=0
biggest_bider=""
for bider in bids:
  if bids[bider]>biggest_bid:
    biggest_bid=bids[bider]
    biggest_bider=bider
print(f"the winner is {biggest_bider}, by the price ${biggest_bid}")