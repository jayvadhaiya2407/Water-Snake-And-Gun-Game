#Importing Moduls
import random

#Globel Variables
com_score = 0
player_score = 0
draws =0 

#Computer Player
def com_player():
	players = [1, 2, 3]
	res = random.choice(players)
	return res
	
#Menu Function
def menu():
	print("\n<--- Select Any One --->")
	print(">>1.  Water")
	print(">>2.  Snake")
	print(">>3.  Gun")
	print("<--- ************** --->")
		
#Player
def player():
	response = int(input("\nEnter Your Choice :\n"))
	return response

#Resuls Function
def results():
	print(f"--> Draws {draws}")
	print(f"--> You Won {player_score} Poins")
	print(f"--> Computer Won {com_score} Poins")

	if com_score > player_score:
		print(f"\n--> You Lose The Game With {com_score-player_score} Points")
	else:
		print(f"\n--> You Won The Game With {player_score-com_score} Poins")
		
#Displaying Selections
def selections(a,b):
	if a == 1:
		print("\nComputer :- Water")
	elif a == 2:
		print("\nComputer :- Sneck")
	else:
		print("\nComputer :- Gun")
		
	if b == 1:
		print("You \t:- Water")
	elif b == 2:
		print("You \t:- Sneck")
	else:
		print("You \t:- Gun")
	
#Starting Of The Game
jk = 0
while jk < 10:
	a = com_player()
	menu()
	b = player()
	selections(a,b)
	
	if a == b:
		draws+=1
		print("\nDraw Happened!, You Both Get 0 Points")
	elif a == 1 and b == 2:
		print("\nYou Won With 1 Point")
		player_score+=1
	elif a == 1 and b == 3:
		print("\nComputer Won With 1 Point")
		com_score+=1
	elif a == 2 and b == 1:
		print("\nComputer Won With 1 Point")
		com_score+=1
	elif a == 2 and b == 3:
		print("\nYou Won With 1 Point")
		player_score+=1
	elif a == 3 and b == 1:
		print("\nYou Won With 1 Point")
		player_score+=1
	elif a == 3 and b == 2:
		print("\nComputer Won With 1 Point")
		com_score+=1
	else:
		print("\nSomething Went Wrong!!")
	jk+=1
print("\n<---- Game Over ---->") 	
results()			