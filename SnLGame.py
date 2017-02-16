"""Snakes And Ladders Game"""

import random
 
Player1_pos = 0
Player2_pos = 0
Destination = 100
 
START = input("Press 1 or ENTER to START the game: ")
Ladders = {3:39, 10:12, 27:53 , 56:84, 61:99, 72:90}
Snakes = {97:75, 66:52, 63:60, 47:25, 31:4, 16:13}

def Roll_Dice(): 
  
   """Generates a Random number for handling Dice throw"""

   DiceNum = random.randint(1, 6)
   return DiceNum

def checkLadderOrSnake(Player_pos): 

   """Checks for snake or ladder in Player's path"""
  
   if Player_pos < Destination:
      for value in Ladders.keys():
         if value == Player_pos:
            Player_pos = Ladders[value]
            print("HURRAY!! It's Ladder, Climb up ////")
      for value in Snakes.keys():
         if value == Player_pos:
            Player_pos = Snakes[value]
            print("OOPsss!! It's Snake, Go down _____")
   return Player_pos

def possibleMove(Player_pos):
   
   """To find the new position of player"""
    
   Player_pos = checkLadderOrSnake(Player_pos)
   return Player_pos



def playBegins(Player_pos, Name):

   """The game begins with this function call"""
    
   if Player_pos != Destination:
      GAME_OVER = False
      print("\n->Chance of Player",Name)
      player = input("# Press ENTER button to Roll the Dice")
      DiceNum = Roll_Dice()
      print('->Player:',Name,'number after dice roll is',DiceNum)
      Player_pos += DiceNum
      Player_pos = possibleMove(Player_pos)
      if Player_pos == Destination:
         print("**CONGO!!Player",Name,"Won**" )
      elif Player_pos > Destination:
         Player_pos -= DiceNum
      print('Current Position of Player:',Name, 'is',  Player_pos)
   return Player_pos, GAME_OVER

GAME_OVER = False
while not GAME_OVER:
   Name1 = 1
   Player1_pos, GAME_OVER = playBegins(Player1_pos, Name1)
   if Player1_pos == Destination:
     break
   Name2 = 2
   Player2_pos, GAME_OVER = playBegins(Player2_pos, Name2)
   if Player2_pos == Destination:
     break
