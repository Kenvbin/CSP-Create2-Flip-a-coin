import random

score = []
correct_side = []
player_side = []
numright = 0
total = 0



def flip_acoin(ammount, statty):
  global score
  for i in range(ammount):
    player_guess = input("Heads or Tails? (h/t): ")
    if player_guess == "h":
      playerguessnum = 1
      player_side.append("Heads")
    elif player_guess == "t":
      playerguessnum = 0
      player_side.append("Tails")
    headortail = random.randint(0,1)
    if headortail == 1:
      correct_side.append("Heads")
    else:
      correct_side.append("Tails")
    if playerguessnum == headortail:
      playerguessnum = 1
      print("\n Your guess was correct! \n")
    else:
      playerguessnum = 0
      print("\n Sorry you were wrong \n")
    score.append(playerguessnum)
  
  if statty == "y":
    numtime = 1
    for item in score:
      print("Round ", numtime, "Correct answer:", correct_side[numtime - 1], "Your Guess:", player_side[numtime - 1], "\n")
      numtime = numtime + 1
  else:
    print("User did not want to see round stats")
  print_shortstat()
  score.clear()
  correct_side.clear()
  player_side.clear()

def print_shortstat():
  global total, numright
  for item in score:
    if item == 1:
      numright = numright + 1
    total = total + 1
  
  finaltotal = "{:.2f}".format((numright/total) * 100)
  
  print("Final Score", finaltotal + "%", "Correct", "\n")
print("Welcome to the flip a coin guess game! \n")

player_wanted_ammount = int(input("How many games of heads or tails would you like to play: "))
player_want_stat = input("At the end of the game would you like your round stats? (y/n): ")
print("")
flip_acoin(player_wanted_ammount, player_want_stat)

player_keepplay = input("Would you like to keep playing (y/n): ")
while player_keepplay != "n":
  player_wanted_ammount = int(input("How many more games of heads or tails would you like to play: "))
  player_want_stat = input("At the end of the game would you like your round stats? (y/n): ")
  print("")
  flip_acoin(player_wanted_ammount, player_want_stat)
  player_keepplay = input("Would you like to keep playing (y/n): ")

print("\n Thank you for playing my coin flip game")