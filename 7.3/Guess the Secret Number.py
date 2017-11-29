secret = "7"

while True:
    guess = raw_input("Guess a number from 0 to 10: ")
    if guess == secret:
        print "Congratulations! You are right!"
        break
    else:
        print "You are wrong! Another try?"

