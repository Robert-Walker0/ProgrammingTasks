

def fizz_buzz(value):
    if(value % 3 == 0 and value % 5 == 0):
        print("FizzBuzz")
    elif(value % 3 == 0):
        print("Fizz")
    elif(value % 5 == 0):
        print("Buzz")
    else: 
        print(value)


def main():
    # Runs the Fizz Program for in between the numbers 0 - 1000
    for i in range(0, 1000 + 1):
        fizz_buzz(i)

#main()

fizz_buzz(0)