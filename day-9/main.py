from util import logo, clear

bids = []
anotherBid = False

print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $ "))
bids.append({
  "name": name,
  "bid": bid
})

otherBid = input("There is another Bid? press y to say yes, otherwise stop.").lower()

if otherBid == 'y':
  anotherBid = True

while anotherBid:
  clear()
  print(logo)
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $ "))
  bids.append({
    "name": name,
    "bid": bid
  })

  otherBid = input("There is another Bid? press y to say yes, otherwise stop.").lower()

  if otherBid != 'y':
    anotherBid = False

maxBid = {
  "name": "",
  "bid": 0
}
for user in bids:
  if user["bid"] > maxBid['bid']:
    maxBid["name"] = user["name"]
    maxBid["bid"] = user["bid"]

print(f"The winner is {maxBid['name']} with a bid of ${maxBid['bid']}")