

drinks = ["Water", "Beer", "Milk", "Soda", "Apple Juice"]

def select_drink():
	for i in range(len(drinks)):
		print("{}. {}".format(i+1, drinks[i]))

	drink = int(input("Enter an option: "))
	if(drink > 0 and drink <= 5):
		return drinks[drink-1]
	if(drink > 5):
		return "Ladder"

	return select_drink()

def main():
	print("What drink would you like to choose for the song?")
	drink = select_drink()

	if drink != "Ladder":
		for i in range(99, 0, -1):
                        if i == 1:
                                print(f"1 bottles of {drink} on the wall!")
                                print(f"1 bottles of {drink}!")
                                print(f"You take one down, pass it around.")
                                print(f"Go to the store and buy some more, 99 bottles of {drink} on the wall...")
                        else:
                                print(f"{i} bottles of {drink} on the wall!")
                                print(f"{i} bottles of {drink}!")
                                print(f"You take one down, pass it around.")
                                print(f"{i-1} bottles of {drink} on the wall.")
			
	else:
		for i in range(99, 0, -1):
			if i == 1:
				print("1 Ladder on the wall!")
				print("1 Ladder")
				print(f"You take one down, pass it around.")
				print(f"Go to the store and buy a stepladder, Nick!")
			else:
                                print(f"{i} Ladders on the wall!")
                                print(f"{i} Ladders")
                                print(f"You take one down, pass it around.")
                                print(f"{i-1} Ladders on the wall.")
			

if __name__ == "__main__":
	main()
	input("Press Enter to exit")
	