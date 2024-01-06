

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


def main():
    print("Enter a word below this, we will tell you if it is a Palindrome or not.")

    try:
        word = input("Enter your word: ")
    except EOFError as Ctrl:
        print("Exiting the program.")
        quit()
    else:
        print(is_palindrome(word))

    input("Press Enter to exit...")

main()


