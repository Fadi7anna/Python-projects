print("Welcome to Philosophy literature quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":  #lower() & upper() methods
    quit()

print("Okay! let's play.. :) ")
score = 0

answer = input("Who invented Logic? ") #OR, alternatively, we can put lower() method in the input().lower()
if answer.lower() == "aristotle":
    print('Correct!')
    score += 1
else:
     print('Incorrect!')


answer = input("Who wrote The Republic? ")
if answer.lower() == "plato":
    print('Correct!')
    score += 1
else:
     print('Incorrect!')


answer = input("Who wrote Das Kapital? ")
if answer.lower() == "marx":
    print('Correct!')
    score += 1
else:
     print('Incorrect!')


answer = input("Who Killed God? ")
if answer.lower() == "nietzsche":
    print('Correct!')
    score += 1
else:
     print('Incorrect!')



print(f"You're a philosophy guy. You got {score} questions correct!")  #OR "..." + str(score) + "..."
print(f"You got {score/4*(100)} %.")