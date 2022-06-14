"""
Name(s): Lynn
Name of Project: Fever Dream ;-;
"""
import random


# setup
import random
def event_roll():
  e = random.randint(1, 10)
  
def events():
  if event_roll == 1:
    print("\nYou walk until you find a village. Night arrived while you walked and you see the full moon rise above. An annual festival takes place during the night-- children in colorful robes run around, long hair trailing behind them. A girl points at the moon. \n\nYour Friend follows you around town as you check out the festivities. The Guide smiles.")
    answer1 = input("\"Strange Traveller, do you know what festival this is?\"")
    if answer1 == "Mid-Autumn Festival" or "Mid Autumn Festival":
      print("\"You're right...\"")
      print("\nThe Guide leads you past the cobblestone paths of the village. Eventually, you reach fields with both large and small craters. The ground was a pale white. It reminded you somehow, of a night sky. You feel light, as if you could float away. The Guide smiles. Your vision turns white.")
    else:
      print("Not quite.")
    
  elif event_roll == 2:
    print("\nYou find yourself at a tavern after a long day of travelling. The Guide gives the owner a few coins. You are lead to a room before being split up from The Guide and your Friends. ")
  elif event_roll == 3:
    print()
  elif event_roll == 4:
    print()
  elif event_roll == 5:
    print()
  elif event_roll == 6:
    print("")
  elif event_roll == 7:
    print("")
  elif event_roll == 8:
    print()
  elif event_roll == 9:
    print()
  elif event_roll == 10:
    print()

def north():
  print("You move north.")
  event_roll()
  events()

def south():
  print("You move south.")
  event_roll()
  events()

def east():
  print("You move east.")
  event_roll()
  events()

def west():
  print("You move west.")
  event_roll()
  events()

  
def direction_op():
  dir = input("north, east, west, south: ")
  if dir == "north":
    north()
  elif dir == "east":
    print("east")
  elif direction == "west":
    print("west")
  elif direction == "south":
    print(south)


#structure
name = input("Hello, strange traveller. What is your name? ")
print("Welcome,", name + ". What road will you take?")
direction_op()