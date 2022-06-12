"""
Name(s): Lynn
Name of Project: Fever Dream ;-;
"""
import random
response = 0
choice3a = 0
choice3b = 0


name = input("Hello, strange traveller. What is your name? ")
print("Welcome,", name + ". What road will you take?")

choice1 = input("left or right? ")
choice1 = choice1.lower() 

if choice1 == "escape": 
  print("\nDid you think you can really escape fate? Begone.")
if choice1 == "42":
  print("\nThe answer to this universe is...")
  print("\nYou wake up suddenly. You are sitting in a classroom. Trigonometry is scrawled all over the paper you were sleeping on... I guess you won't pass the next test, huh.")

if choice1 == "left":
  print("\nYou reach the split and take the left. Out of the corner of your eye, you see a phantom flit towards the right.")
  choice2 = input("\nDo you follow? (yes, no) ")
  choice2 = choice2.lower()
elif choice1 == "right":
  print("\n\"Good choice\".\nThe left road fades. You walk forward. \nYou see a stray cat strolling through the trees.")
  choice2 = input("\nDo you follow? (yes, no) ")
  choice2 = choice2.lower()

if choice1 == "left" and choice2 == "yes":
  print("\nYou follow the phantom into the woods. They take the right instead of the left. \n\nThe sun overhead starts setting, turning the trees a strange shade of red. You continue running. Eventually, you reach a hut. The phantom disappears-- were you imagining the whoel scenario? Outside, a cat with gleaming white fur licks its paw.")
  choice3a = input("\nWould you like to explore the hut? (yes, no)")
  choice3a = choice3a.lower()
elif choice1 == "left" and choice2 == "no":
  print("\nYou continue on with the left path. With each step, the path grows more narrow, the trees closing in on you. You continue walking, feet becoming heavier and heavier. Eventually, you reach a dead end surrounded by trees. You stand there, considering your options. As you do, the path disapears beneath your feet. You can no longer turn back.")
  choice3a = input("\nWalk towards left or right? ")
  choice3a = choice3a.lower()
elif choice1 == "right" and choice2 == "yes": 
  print("\nYou follow the phantom into the woods. They take the right instead of the left. \n\nThe sun overhead starts setting, turning the trees a strange shade of red. You continue running. Eventually, you reach a hut. The phantom disappears-- were you imagining the whoel scenario? Outside, a cat with gleaming white fur licks its paw.")
  choice3a = input("\nWould you like to explore the hut? (yes, no)")
  choice3a = choice3a.lower()
elif choice1 == "right" and choice2 == "no":
  print("\nYou wander around and eventually find a hut You are quite tired. Would you like to explore?.")
  choice3a = input("\nWould you like to explore the hut? (yes, no)")
  choice3a = choice3a.lower()

if  choice1 == "right" and choice2 == "no" and choice3a == "yes":
  print("\nYou open the door-- part of it cracks off. Looking down, you see that it is made of gingerbread. Ignoring that, you walk in.")
  print("\n\"Hello,\" a witch rasps. \nYou look over at her. How did you know she is a witch? You can't remember. You decide to explore the hut as you planned to.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
elif  choice1 == "right" and choice2 == "no" and choice3a == "no":
  print("\nYou decide to continue walking. There is nothing but trees for miles to come. Eventually, you black out from exhaustion and lack of food or water...")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()


if choice1 == "left" and choice2 == "yes" and choice3a == "yes": 
  print("\nYou open the door-- part of it cracks off. Looking down, you see that it is made of gingerbread. Ignoring that, you walk in.")
  print("\n\"Hello,\" a witch rasps. \nYou look over at her. How did you know she is a witch? You can't remember. You decide to explore the hut as you planned to.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()
if choice1 == "left" and choice2 == "yes" and choice3a == "no": 
  print("\nYou decide to continue walking. There is nothing but trees for miles to come. Eventually, you black out from exhaustion and lack of food or water...")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()


if choice1 == "right" and choice2== "yes" and choice3a == "no":
  print("\nYou continue walking... and walking... and walking... eventually you faint from hunger and dehydration.")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()
  
if choice1 == "left" and choice2 == "no" and choice3a == "left":
  print("\nYou continue walking. There is nothing but trees for miles to come. Eventually, you black out from exhaustion and lack of food or water...")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()


if choice1 == "right" and choice2== "no" and choice3a == "no":
  print("\nYou continue walking... and walking... and walking... eventually you faint from hunger and dehydration.")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()
elif choice1 == "right" and choice2 == "yes" and choice3a == "yes":
  print("\nYou enter the hut. A witch stands in the corner, making something in the kitchen.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()
elif choice1 == "right" and choice2 == "no" and choice3a == "right":
  print("\nYou continue walking. There is nothing but trees for miles to come. Eventually, you find a small rest station. A hooded figure sits there...")
  print("\n\"Hello there.\"")
  response = input("What is your response? (hint, the correct one is 2 words) ")
  response = response.lower()

if choice1 == "left" and choice2 == "no" and choice3a == "right" and response =="general kenobi":
  print("\n The hooded figure smiles. \n\n\"Well I'm glad you understood my reference. It is rare to meet another traveler such as myself.\"")
  print("\nThe hooded figure stands up from the bench.")
  print("\n\"The way out is to escape from the start.\"")
  print("\nThe hooded figure vanishes.")
  print("\n\n\n\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()

if choice1 == "right" and choice2 == "yes" and choice3a == "yes" and choice3b == "yes":
  print("\nYou open the door-- part of it cracks off. Looking down, you see that it is made of gingerbread. Ignoring that, you walk in.")
  print("\n\"Hello,\" a witch rasps. \nYou look over at her. How did you know she is a witch? You can't remember. You decide to explore the hut as you planned to.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()

elif choice1 == "left" and choice2 == "no" and choice3a == "right":
  print("\nYou continue walking. There is nothing but trees for miles to come. Eventually, you find a small rest station. A hooded figure sits there...")
  print("\n\"Hello there.\"")
  response = input("What is your response? (hint, the correct one is 2 words) ")
  response = response.lower()
  
if response != "general kenobi" and choice1 == "left" and choice2 == "no" and choice3a == "right":
  print("\nUnfortunately, you must've answered wrong. You are somehow lifted up and tossed against a bench. The hooded figure stands in front of you, a silver glint at the hip. You see a blue light before you pass out...")
  print("\nYou wake up in a room. A witch stands in the corner, making something in the kitchen. You stand up from the large armchair.")
  print("\nLooking around, you see a fireplace in the far left corner. You also see a overly large oven. Huh. You walk further into the hut, ignoring the witch.")
  print("\nYou notice a door on the opposite wall. Maybe it leads to the backyard? The hut was rather small.")
  choice3b = input("Do you open the door? (yes, no) ")
  choice3b = choice3b.lower()

if choice3b == "yes":
  print("\nYou open the door and walk in. The bedroom inside is stunning-- it even had it's own fireplace! Wait a sec... a fireplace? \n\nThe door shuts behind you... the fire starts (when did witches gain electric fireplaces? Oh wait magic-).")
  print("\nThe room gets warmer and warmer. You start feeling sleepy, your head turns fuzzy, and your legs give in. The witch cackled happily outside, ready to consume human toast. The world turns black.")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"Dear traveler, how many times have you tried playing this game?\" The guide from the beginning smiles at you.")
  numoftimes = input("Enter number of times... ")
  print("\n" + numoftimes + "\"times...\" the guide sighs. ")
  print("\nFate is already decided... the only thing that changes is how you get there. Although if you don't give up, the directions to the clue is quite easy.")
  print("First, remember The Creator's name and then remember Triangles. The most beloved Triangle is one that is Not Wrong.") #i feel so narcassistic... but i did create this so HA

if choice3b == "no":
  food = "The witch offers you food and drink. Tired, you drink it. The world fades into black... \nYou wake up in a room. Why is it so warm...?"
  nofood = "The witch offers you food and drink. Tired, but suspicious, you turn down the offer. The witch smiles and walks out of the hut. You feel warm... and slowly black out."
  yorn = [food, nofood]
  print(random.choice(yorn))
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"Dear traveler, how many times have you tried playing this game?\" The guide from the beginning smiles at you.")
  numoftimes = input("Enter number of times... ")
  print("\n" + numoftimes + "\"times...\" the guide sighs. ")
  print("\nFate is already decided... the only thing that changes is how you get there. Although if you don't give up, the directions to the clue is quite easy.")
  print("First, remember The Creator's name and then remember Triangles. The most beloved Triangle is one that is Not Wrong.")

