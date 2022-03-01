print("Welcome to the Quiz Game")
playing = input("Do you interested to play the game?  ")
if playing.lower() != "yes":
    quit()
print("OK! Let's play the game")
score = 0

# Question Section
answer = input("Which city is the capital of Bangladesh?  ")
if answer.lower() == "dhaka":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Which is the longest sea beach in the world?  ")
if answer.lower() == "cox's bazar":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("Which is the largest mangrove forest in the world?  ")
if answer.lower() == "the sundarbans":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How many divisions has  Bangladesh?  ")
if answer.lower() == "8" or "eight":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Result Section
print("You got " + str(score) + " correct answer")
print("Thank You for plying the game")
