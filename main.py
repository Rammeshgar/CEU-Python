
from replit import clear
from  art import logo
import random


def guess_me():
  print(logo)
  print("\nWelcome to the Number Guessing Game!")
  print("\nI'm thinking of a number between 1 and 100.")
  number=int(random.randint(1,100))
  #print(number)
  level=input("\nChoose a difficulty. Type E ('easy' = 10 chances) or Type H ('hard' = 5 chances): ").lower()
  
  if level=="h":
    life=5
  elif level=="e":
    life=10
  else:
    print(f"you typed {level}, considered as easy.")
    life=10

  
  while life > 0:
    print(f"\nyou have {life} life!")
    user=int(input("\nguess a number. "))
    
    if user==number:
      print(f"\n\nThe secret number is {number}\n\ncorrect. you win!!")
      restart = input("\nwould you play another round? (y,n) ").lower()
      if restart=="y":
        clear()
        guess_me()
      elif restart=="n":
        print("\n\nGame Over!")
        return"tamam"
        break

    elif (user+1) <= number < (user+4):
      life-=1
      print(f"\nyou're so close!")
    elif (user+4) <= number < (user+11):
      life-=1
      print(f"\nyou're close, a little bit higher.")
    elif user+10 < number:
      life-=1
      print(f"\ntoo low. guess again")
    elif (user-10) <= number < (user-3):
      life-=1
      print(f"\nyou're close, a little bit lower.")
    elif (user-3) <= number < (user-0):
      life-=1
      print(f"\nyou're so close!")
    elif user-10 > number:
      life-=1
      print(f"\ntoo high. guess again")

  
  if life==0:
    print(f"\ngame over! \n\nthe correct number is {number}")
    restart = input("\nwould you play another round? (y,n) ") 
    if restart=="y":
      clear()
      guess_me()
    elif restart=="n":
      return"Game over"
    
#Number Guessing Game Objectives:

guess_me()



# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

