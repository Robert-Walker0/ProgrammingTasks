import random

OPTIONS = ["rock", "paper", "scissors"]

def select():
	print("Choosing anything else besides the three will result in asking for more input for the game: ")
	user_choice = input("Select Rock, Paper or Scissors: ")
	return user_choice.lower() if user_choice.lower() in OPTIONS else select()

def main():
	print('Rock, Paper, Scissors, Shoot!')
	selection = select()
	computer_decision = random.choice(OPTIONS)
	print(f"{selection} vs {computer_decision}")
	if((selection == "rock" and computer_decision == "paper") or (selection == "paper" and computer_decision == "scissors") or (selection == "scissors" and computer_decision == "rock")):
		print("Computers Wins!")
	elif selection == computer_decision:
		print("Tie!")
	else:
		print("You Win!")
	input("Press Enter to exit...")
		

if __name__ == '__main__':
	main()

