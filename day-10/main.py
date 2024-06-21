from operations import *
from art import logo

operations = {
  "+": add,
  "-":sub,
  "*": mult,
  "/": divide
}


def calculator():
  print(logo)
  x = float(input("What's the first number?: "))
  for operation in operations:
    print(operation, end=" | ")
  print()

  should_continue = True

  while should_continue:
    operation_choice = input("Pick an operation from the list above: ")
    y = float(input("What's the second number?: "))
    calculation_operation = operations[operation_choice]

    answer = calculation_operation(x,y)

    print(f"{x} {operation_choice} {y} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or other key to start a new calculation: ") == "y":
      x = answer
    else:
      should_continue = False
      calculator()


calculator()