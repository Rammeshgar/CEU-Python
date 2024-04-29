
import random

#from art import logo
#print(logo)
list_game = list(range(2, 12))

user = input("do you wanna play blackjack? (y,n) ")
user_card = 0
pc = 0

user_random = random.choices(list_game,weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.04, 0.01],k=2)
pc_random = random.choices(list_game,weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.04, 0.01],k=2)

game_on=True
while game_on == True:
  user_random_new = random.choices(
    list_game,
    weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.04, 0.01],
    k=1)
  pc_random_new = random.choices(
    list_game,
    weights=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.04, 0.01],
    k=1)
  
  if user == "y":
    for i in user_random:
      user_card += i
      userR = user_card
    for i in pc_random:
      pc += i
      pcR = pc
      print(f"your card is: {userR} computer card is: {pc}")
    if pcR > 21:
      print("computer lost, \nyou win!")
      game_on = False
    elif userR > 21:
      print("your score is above 21, \nyou lose!")
      game_on = False
    elif pcR == userR and userR > 21:
      print("you are both over 21, \ngame draw")

  user = input("do you wanna new card? (y,n) ")
  if user == "y":
    user_card = userR
    pc = pcR
    user_random_new = user_random
    pc_random_new = pc_random
  else:
    if pcR == userR and pcR < 22:
      print(f"yor card is: {userR} computer card is: {pcR} \ngame draw")
      game_on = False
    elif pcR < userR:
      print(f"you got higher score: {userR} ,computer:{pcR} \nyou win!")
      game_on = False
    elif pcR > userR:
      print(f"you got the lower score: {userR} ,computer:{pcR} \nyou lose!")
      game_on = False

