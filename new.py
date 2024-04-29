from art import logo, vs
from game_data import data
import random

game_on = True

def game():
  while game_on==True:
    print(logo)
    user_score=0
  
    for i in data:
      choice_A=random.choice(data)
      choice_B=random.choice(data)
      
      print(choice_A["name"],choice_A["description"],choice_A["country"])
      print(vs)
      print(choice_B["name"],choice_B["description"],choice_B["country"])
      
      count_A=choice_A["follower_count"]
      count_B=choice_B["follower_count"]
    
      user = input("What is your choice? (A/B)").lower()
      
      if user=="a":
        user=count_A
        pc=count_B
      elif user=="b":
        user=count_B
        pc=count_A
      
      if user > pc:
        user_score+=1
        print(user_score)
      else:
        print("you lost")
        print(user_score)
        restart = input("\nwould you start a new game? (Y/N) ").lower()
        if restart=="y":
          game()
        else:
          global game_on
          game_on=False

game