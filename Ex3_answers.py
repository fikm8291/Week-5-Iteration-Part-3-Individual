# -------------------------------------------
# Exercise 3: Answers
# -------------------------------------------
# This file contains answers with explanations.
# Use this to check your own work and learn from the comments.
# -------------------------------------------


# -------------------------------------------
# Task 1: Collect Multiple Inputs
# -------------------------------------------

# Ask for three friends' names and greet each one
friend1 = input("Enter the name of your first friend: ")
friend2 = input("Enter the name of your second friend: ")
friend3 = input("Enter the name of your third friend: ")

# Put all three names into a list
friends = [friend1, friend2, friend3]

# Use a for loop to greet each friend
for name in friends:
    print("Hello", name)  # Loops through the list and prints each greeting

# NOTE: A list makes it easier to use loops later for more names!


# -------------------------------------------
# Task 2: Number Input and Decisions
# -------------------------------------------

# Ask the user to enter a number between 1 and 10
number = int(input("Enter a number between 1 and 10: "))

# Keep asking until the number is in the valid range
while number < 1 or number > 10:
    print("Invalid number, try again.")
    number = int(input("Enter a number between 1 and 10: "))

# Once valid, print the correct message
if number < 1:
    print("That’s too low!")  # Won’t actually happen because of while loop
elif number > 10:
    print("That’s too high!")  # Won’t happen either
else:
    print("Nice! That number is in range.")  # This prints once it’s valid

# NOTE: The while loop checks that the number stays between 1 and 10.


# -------------------------------------------
# Task 3: Mini Quiz Project Using a List
# -------------------------------------------

# Create a list of questions
questions = ["What is 2 + 2? ", "What colour is the sky? ", "First letter of the alphabet? "]

# Go through each question using a loop
for q in questions:
    answer = input(q)

    # Use if/elif/else for feedback
    if q == "What is 2 + 2? " and answer == "4":
        print("Correct!")
    elif q == "What colour is the sky? " and answer == "blue":
        print("Good job!")
    elif q == "First letter of the alphabet? " and answer == "a":
        print("Exactly right!")
    else:
        print("Check your answer.")


# -------------------------------------------
# Extension 1: Input Validation
# -------------------------------------------

answer = input("Enter your favorite fruit: ")

# Keep asking until something is typed
while answer == "":
    print("You must type something.")
    answer = input("Try again: ")

print("Your favorite fruit is:", answer)

# NOTE: An empty string "" means the user pressed Enter without typing anything.


# -------------------------------------------
# Extension 2: Multiple Feedback Options
# -------------------------------------------

answer = input("Type A, B, or C: ")

# Keep asking until the input is valid
while answer not in ["A", "B", "C"]:
    print("Invalid choice. Please type A, B, or C.")
    answer = input("Type A, B, or C: ")

# Use if/elif/else for feedback
if answer == "A":
    print("You chose option A — great choice!")
elif answer == "B":
    print("You picked B — nice!")
else:
    print("You went with C — interesting!")

# NOTE: Lists are handy for checking valid options like this.


# -------------------------------------------
# Extension 3: Repeat Quiz for Another User
# -------------------------------------------

questions = ["What is 2 + 2? ", "What colour is the sky? ", "First letter of the alphabet? "]

# Ask for first user’s name
user = input("Enter your name: ")

# Use a while loop to allow multiple users
while user != "":
    print("Welcome,", user + "!")
    for q in questions:
        answer = input(q)
        if q == "What is 2 + 2? " and answer == "4":
            print("Correct!")
        elif q == "What colour is the sky? " and answer.lower() == "blue":
            print("Good job!")
        elif q == "First letter of the alphabet? " and answer.lower() == "a":
            print("Exactly right!")
        else:
            print("Check your answer.")
    print("Quiz complete for", user)
    user = input("\nEnter another user's name (or press Enter to stop): ")

print("All quizzes done!")

# NOTE: Pressing Enter without typing a name ends the quiz loop.


# -------------------------------------------
# ADVANCED TASK: Combine Everything
# -------------------------------------------

# Step 1: Greet three friends
friends = []
for i in range(3):
    name = input(f"Enter friend {i+1} name: ")
    friends.append(name)
for name in friends:
    print("Hello", name)

# Step 2: Ask for a number between 1 and 10
number = int(input("\nEnter a number between 1 and 10: "))
while number < 1 or number > 10:
    print("Invalid number. Try again.")
    number = int(input("Enter a number between 1 and 10: "))
print("Thank you! Your number is valid.")

# Step 3: Run a mini quiz
questions = ["What is 5 + 5?", "What colour is grass?", "First month of the year?"]
for q in questions:
    answer = input(q + " ")
    if q == "What is 5 + 5?" and answer == "10":
        print("Correct!")
    elif q == "What colour is grass?" and answer == "green":
        print("Good job!")
    elif q == "First month of the year?" and answer == "january":
        print("Nice work!")
    else:
        print("Check your answer.")

print("\nAll tasks complete! Great job practicing loops and decisions.")
