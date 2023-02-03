# Computer quiz game

print("Welcome to my quiz!")

# variable playing and asking for user input
playing = input("Do you want to play? ")

# if user wants to play, continue. if not, quit.
if playing.lower() != "yes":
    quit()

print("Yay! Let's play :)")
score = 0

# Question 1
answer1 = input("What does CPU stand for? ")
if answer1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong :( ")

# Question 2
answer2 = input("What does GPU stand for ")
if answer2.lower() == "graphics processing unit":
    print("Ding Ding Ding!")
    score += 1
else:
    print("Try Again :( ")

# Question 3
answer3 = input("What does RAM stand for? ")
if answer3.lower() == "random access memory":
    print("You Got It!")
    score += 1
else:
    print("Incorrect :( ")

print("You got " + str(score) + "  questions right!")
print("You got " + str((score / 3) * 100) + "%.")