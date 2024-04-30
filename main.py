alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
'''
def code(plain_text, shift_amount):
  if direction == "encode":
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode":
    real_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      real_text += alphabet[new_position]
    print(f"The decoded text is {real_text}")
'''

def code(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction=="encode":
      new_position = position + shift_amount
    elif direction=="decode":
      new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")
  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
code(text, shift)
