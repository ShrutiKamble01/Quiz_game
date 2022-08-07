print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Lets Play :) ")
score = 0

ans = input("what does CPU stands for? ")
if ans.lower() == "central processing unit":
    print('Correct ans!')
    score += 1
else:
    print('Incorrect!')

ans = input("what does GPU stands for? ")
if ans.lower() == "graphic processing unit":
    print('Correct ans!')
    score += 1
else:
    print('Incorrect!')

ans = input("What does RAM stand for? ")
if ans.lower() == "random access memory":
    print('Correct ans!')
    score += 1
else:
    print('Incorrect!')

ans = input("What does PSU stand for? ")
if ans.lower() == "power supply unit":
    print('Correct ans!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' question correct!')
print('You got ' + str((score /4)*100) + ' %')


