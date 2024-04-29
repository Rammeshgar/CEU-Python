import random

list_game=range(2,12)
random=random.choice(list_game, weight=[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.04,0.01],k=1)
print(random)
'''
game_on=True
while game_on==True:
  '''