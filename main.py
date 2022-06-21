"""
Name(s): Lynn
Name of Project: Fever Dream
"""
import random
import time

# setup
import random
def adv():
  a = ["mouse", "friend", "witch"]
  a = random.choice(a)
  b = random.randint(1,2)
  mouse = ["While travelling, you notice that someone is following you.", "You take the path The Guide points out for you. While walking, you hear footsteps behind you. When you turn around you see a flash but it disappears.", "You notice a rustling in the bushes a few minutes into your journey... something seems to be following you."]
  if a == "mouse":
    mouse = random.choice(mouse)
    print("\n", mouse)
    mouse_choice = input("\nDo you choose to hide and wait for the intruder to show themselves? [yes/no] ")
    mouse_outcome = ["You hide but the stalker simply passes by...", "The stalker stops for a bit. When you feel safe and start walking, you hear footsteps behind you.", "You see the stalker... a glimpse of a hooded cloak and nothing more."]
    if mouse_choice == "yes":
      print("\nYou hide after finding a suitable spot.")
    elif mouse_choice == "no":
      print("\nYou chose not to hide but eventually stopped to take a break. You hear leaves crunching...")
    else:
      print("\nUnfortunately the system does not recognize your response... although luckily The Guide has thought of that and rolled a dice to decide your fate.")
      mouse_outcome = random.choice(mouse_outcome)
      print(mouse_outcome)
  elif a == "friend":
    friend = ["fellow traveller", "tavern owner", "dragon", "shrouded figure"]
    friend = random.choice(friend)
    print("\nWhile travelling, you met a " + friend +". They seem to be nice so you took them along on your journey.")
  elif a == "witch":
    print("\nYou meet a witch during your travels. They look haggard, as if they've been following someone for days...")
    f = input("Do you welcome witch or not? [yes/no]")
    e = random.randint(1,2)
    e = str(e)
    f = f+e
    if f == "yes1":
      print("\nThe witch leads you to a well. Through it, you could see a world full of gray buildings and busy people. It was unlike anything here.")
    elif f == "yes2":
      print("The prey the witch was stalking happened to be you... you were stabbed and left for dead. Thankfully, you were saved by The Guide.")
    elif f == "no1":
      print("The prey the witch was stalking happened to be you... you were stabbed and left for dead. Thankfully, you were saved by The Guide.")
    elif f:
      print("The prey the witch was stalking happened to be you... you were stabbed and left for dead. Thankfully, you were saved by The Guide.")
    else:
      print("The system does not recognize the answer... because of that the witch thought you were hostile and murdered you in your sleep. You wake up in front of The Guide again.")

en = [1,2,3,4,5,6,7]
  
def events():
  e = random.choice(en)
  if e == 1:
    print("\nYou walk until you find a village. Night arrived while you walked and you see the full moon rise above. An annual festival takes place during the night-- children in colorful robes run around, long hair trailing behind them. A girl points at the moon. \n\nYour Friend follows you around town as you check out the festivities. The Guide smiles.")
    answer1 = input("\"Strange Traveller, do you know what festival this is?\"")
    answer1 = answer1.title()
    if answer1 == "Mid-Autumn Festival":
      print("\n\"You're right...\"")
      print("\nThe Guide leads you past the cobblestone paths of the village. Eventually, you reach fields with both large and small craters. The ground was a pale white. It reminded you somehow, of a night sky. You feel light, as if you could float away. The Guide smiles. Your vision turns white.")
    if answer1 == "Mid Autumn Festival":
      print("\"You're right...\"")
      print("\nThe Guide leads you past the cobblestone paths of the village. Eventually, you reach fields with both large and small craters. The ground was a pale white. It reminded you somehow, of a night sky. You feel light, as if you could float away. The Guide smiles. Your vision turns white.")
      en.remove(1)
    else:
      print("Not quite.")
    
  elif e == 2:
    print("\nYou find yourself at a tavern after a long day of travelling. The Guide gives the owner a few coins. You are lead to a room before being split up from The Guide and your Friends. ")
    print("\nYou find yourself unable to sleep. You feel like you forgot something...")
    print("\nYou get up and look out the window. The fields seem to have turned barren, orange-red soil poking out the door. A rover is... well... roving around under the unnaturally reddish sky.")
    print("\nAbove your head you see an object in orbit. Underneath, you see a man tilt his head inquisitively at the sky.")
    answer2 = input("\nWhere in the world are you?")
    answer2 = answer2.title()
    if answer2 == "Mars":
      print("\nBut no humans have been on Mars yet have they? You wonder what happened to you...")
      en.remove(2)
    else:
      print("Not quite.")
    print("\nWhen you ask The Guide about the man sitting alone at night, you receive a vague answer.")
    print("\n\"Him? Oh he's just an exiled man who asks Heavenly Questions. I think most of them are unanswerable. Why does he bother asking?\"")
    print("\nHaving no response, you tell The Guide that you wish to travel further. \n\nThe world fades into white.")
  elif e == 3:
    print("\nThe Guide teleported you... but something was wrong.")
    print("\n\"It would appear that I am out of practice... have my insincere apologies. I mean my since-\"")
    print("\nYou gave The Guide a look. The Look. Except you couldn't actually see anything. The Guide was finally silent. You were floating around in something black? Or was it black nothingness?")
    print("\nYou look up and finally in the distance, you see what seemed to be a newly assembled space station. What the hec happened to the ISS?")
    print("\n\"You don't remember? The ISS is going to stop functioning and crash-. Nevermind, just google it.\" The Guide stopped talking.")
    print("\nYou feel infuriated. How are you going to have cell service in the middle of space? How are you still alive???")
    answer3 = int(input("When is the ISS supposed to crash into the pacific? (pls answer the year only, with an integer)"))
    if answer3 == 2030:
      print("\nThat seems about right.")
      en.remove(3)
    else:
      print("\nNot quite.")
    print("\nThe Guide notifies you that you can teleport again. You look at the space station again. It wasn't there. Instead, you catch a glimpse of a towering palace of gold. The world turns white.")
  
  else:
    adv()
def north():
  print("You move north.")
  events()
  time.sleep(15)
  print("\n" * 100)

def south():
  print("You move south.")
  events()
  time.sleep(15)
  print("\n" * 50)

def east():
  print("You move east.")
  events()
  time.sleep(15)
  print("\n" * 50)

def west():
  print("You move west.")
  events()
  time.sleep(15)
  print("\n" * 50)

  
def direction_op():
  dir = input("\nnorth, east, west, south: ")
  if dir == "north":
    north()
  elif dir == "east":
    print("east")
    east()
  elif dir == "west":
    print("west")
    west()
  elif dir == "south":
    print("south")
    south()


#structure
name = input("Hello, strange traveller. What is your name? ")
print("Welcome,", name + ". What road will you take?")
counta = en.count(1)
countb = en.count(2)
countc = en.count(3)
for cont in range(1, 10000):
  if counta > 0:
    direction_op()
  elif countb >0:
    direction_op()
  elif countc > 0:
    direction_op()
  else:
    print("\n"*50)
    print("You wake up after a long day of travelling.")
    print("\nUnable to fall asleep again, you begin to wander around.")
    print("\nYou found a bridge in the middle of nowhere, stretching over a dark chasm.")
    print("A dark figure approaches you.")
    input = ("\n\"Where is this?\"")
    input = ("\n\"Who am I?\"")
    input = ("\n\"What will you do now?\"")
    print("\nThe figure seems to disagree with your answers. It reaches out with a sword to slash at you. The world turns white.")
    print("\n"*100)
    print("You wake up to the sound of Stayin' Alive playing in the background. Your chest hurts for some reason. You groan in dispair. It seems after your little adventure after you choked on water will not save you from taking your finals. Good luck. (At least we don't have a comp sci test right)")





#If a player (other than Mr. Cheng) got curious abt the code and is looking thru it... HA YOU HAD NO REAL CHOICE IN THIS GAME. IT WAS ONLY THE ILLUSION OF CHOICE THAT YOU HAD. The goal is to escape this "world" ig but the reality is that you cannot escape from the real world. AKA me trying not to think abt finals (and failing :D). Also Mr. Cheng if you're reading this... pls don't fail me... you never said the choices players made had to affect the game so very technically they should've made 4 choices (even if it doesnt affect the outcome).

#Anyways if you're wondering abt the weird scenarios I put you thru... it was to get you to do research bc I am a nerd. /j I am not a nerd. But I found it interesting (and kind of funny) how China is naming their space missions. For ex tianwen (heavenly questions) is just this dude asking questions (and if you read thru them and know the context they have no answers). And the mission where they landed the rover on Mars is named after that! You're asking the heavens questions (and now answering them since you're exploring places with the rover or smth.) The missions to explore the moon is named after Chang'e! Just look up the legend and you'll see why if you didn't. Also tian gong = heavenly palace aka the space station China is building. Anyways the point is I found a ton of stuff named after poetry (it started off with a song from a tv show) and anyways tianwen kept on showing up and I found the thingy. I just found it fun how they took myths and stuff from the past and rly just started naming sciency futuristic (except its in the present so like) stuff after it. (Kind of reminds me of the Apollo stuff except everybody knows it so its less fun researching.)