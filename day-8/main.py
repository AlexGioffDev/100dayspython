from util import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


starter = True

def caeser(text, shift, direction):
  message = ""
  if direction == "decode":
    shift *= -1
  for letter in text:
    index = alphabet.index(letter)
    message += alphabet[(index + shift) % len(alphabet)]
  print(f"The {direction}d text is {message}")


print(logo)

while starter:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caeser(text, shift, direction)

  again = input("Write y you want to do again or any other letter if you want to close: ")
  if again.lower() != "y":
    starter = False