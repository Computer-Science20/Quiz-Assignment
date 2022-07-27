# Python Simple Quiz Start

# Score
score = 0

# Question 1
answer1 = input("What is the largest country in the world? ")
if answer1 == "Russia":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Question 2
answer2 = input("What is the smallest country in the world? ")
if answer2 == "Vatican City":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Question 3
answer3 = input("Which country is the most populated around the world? ")
if answer3 == "China":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Question 4
answer4 = input("Which country does the Rocky Mountains exist in? ")
if answer4 == "Canada" or answer1 == "United States":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Question 5
answer5 = input(
    "Which country has the most amount of freshwater compared to the rest of the world? ")
if answer5 == "Brazil":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

# Output Result of Quiz
print("Your score is " + str(score) + " / 5.")

if score == 5:
    print("You got a 100%  Excellent Work!")
elif score == 4:
    print("You got a 80%  Great Job!")
elif score == 3:
    print("You got a 60%  Good Effort!")
elif score == 2:
    print("You got a 40%  You need to pay attention more!")
elif score == 1:
    print("You got a 20%  You need to study everything!")
elif score == 0:
    print("You got a 0%  Did you even try to study??")
