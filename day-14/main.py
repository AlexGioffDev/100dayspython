MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

while(True):
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice.lower() == "report":
    for k, v in resources.items():
      print(f"{k}: {v}")
    print(f"Money: ${money:.2f}")
    continue
  elif choice.lower() == "exit":
    break
  else: 
    while choice.lower() not in MENU:
        print("Invalid choice!")
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    
  while money < MENU[choice]["cost"]:
    print("You dont'have enough money")
    dollar = int(input("How many dollars? "))
    cents = int(input("how many cents? "))
    money += dollar + (cents / 100)
  
  for k,v in MENU[choice]["ingredients"].items():
    if resources[ingredient] < v:
      print(f"Sorry! there is not enough {ingredient}")

  money = money - MENU[choice]["cost"]

  if money > 0.0:
    print(f"Here your rest: ${money:.2f}")
  
  for ingredient, amount in MENU[choice]["ingredients"].items():
    resources[ingredient] -= amount
  print(f"Here your {choice}! enjoy")




  