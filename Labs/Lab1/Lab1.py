__author__ = 'Glenn Contreras'

# Glenn Contreras and Neha Tammana worked together

def getContents(path):
        with open(path) as file:
            content = file.read()
            return content.splitlines()

def encrypt(input):
    secret = []
    for letter in input:
        if letter.isalpha():
            secret.append({"letter": letter, "found": False})
        else:
            secret.append({"letter": letter, "found": True})
    return secret

def displaySecret(secret):
    for letter in secret:
        if letter.get("found"):
            print(letter.get("letter"), end="")
        else:
            print(" _ ", end="")
    print()

def getInput(msg):
    while True:
        print("Enter 'quit' to exit")
        userInput = input(msg)
        if len(userInput) == 1 and userInput.isalpha():
            return userInput
        elif userInput == 'quit':
            quit()
        print("Invalid input")

def toggle(guess, secret):
    found = False
    for item in secret:
        if item.get("letter").lower() == guess.lower():
            item["found"] = True
            found = True
    return found

def isWinner(secret):
    # if one is not found then return False
    for item in secret:
        if not item.get("found"):
            return False
    return True

def main():
    import random

    capitals = getContents("capitals.txt")
    rand = random.randrange(len(capitals)-1)
    capital = capitals[rand]
    secret = encrypt(capital)

    attempts = 10
    guesses = []

    while not isWinner(secret):
        if attempts > 0:
            print("Lives: {}".format(attempts))
            displaySecret(secret)

            print("Letters guessed: {}".format(guesses))
            guess = getInput("Please enter a letter:")

            if guess in guesses:
                print("You already guessed that.\n")
                continue
            else:
                guesses.append(guess)

            if not toggle(guess, secret):
                attempts -= 1

            print()

        else:
            print("Sorry, you ran out of attempts. \nThe correct answer: {}".format(capital))
            break
    else:
        print(capital)
        print("Congrats! You won!")

if __name__ == "__main__":
    main()

