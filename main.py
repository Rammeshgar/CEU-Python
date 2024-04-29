from replit import clear
import shutil
from art import art

columns = shutil.get_terminal_size().columns

print(f"{art}\n\n".center(columns))
print("---The balance index is between '9-12'---\n\n\n".center(columns))
another=True
while another:
  
  a = float(input("\nwhat is your size?(cm)"))
  b = float(input("\nwhat is your height?(cm)"))
  point = b / a
  
  print(f"\nyour index is {point}")
  if point > 12:
    if point > 13.5:
      print("\nthere in NO Hope! belive it!")
    else:
      print("\nYour size is too small.!!")
  elif point < 12:
    if point < 9:
      print("\nRespect! You are one of the legends!!")
    else:
      print("\nSuch a MAN.! ")
  elif point == 12:
    print("\nYou perhaps survive, best of luck...")
  else:
    print("\nEnter the size in number")
  another = input("\nwould you check again?(Y/N)").lower()
  if another=="n":
      another=False
  elif another =="y":
    clear()
