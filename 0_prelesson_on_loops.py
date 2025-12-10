# Example Practice:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))

# Challenge: print each fruit on a new line
for fruit in fruits:
    print(fruit)


# -----------------------------------------
# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]

for subject in subjects:
    if subject == "history":   # <- this will never trigger because of lowercase
        break
    print(subject)

# Correct version if you WANT it to break on History:
# for subject in subjects:
#     if subject.lower() == "history":
#         break
#     print(subject)


# Challenge:
# Use a for loop and range to print each subject with its index
for index in range(len(subjects)):
    print(f"Subject {index}: {subjects[index]}")


# -----------------------------------------
# Print numbers 1 to 600
list1000 = list(range(1, 1001))
for num in list1000:
    if num > 600:
        break
    print(num)


# -----------------------------------------
# FIXING your broken code:
# You had: "if list 101 <= 505:" (invalid variable name)

list101 = list(range(1, 10000))
for num in list101:
    if num > 505:
        break
    print(num)


# -----------------------------------------
# Given:
numbers = [5, 10, 15, 20]

# Challenge: add all numbers using a for loop
total = 0
for number in numbers:
    total += number

print("Total:", total)


# -----------------------------------------
# Credit applicants:
applicants_for_credit = ["Alice", "Bob", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610, 750]

# zip the two lists and skip anyone below 600
for applicant, score in zip(applicants_for_credit, credit_scores):
    if score < 600:
        continue
    print(f"{applicant} approved for credit with a score of {score}.")

subjects = ["Math", "Science", "History", "Art"]

for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])

#given

total = 0
for number in numbers:
    # add each number to total
    total += number
    #shortand for total = total + number
print("Total:", total)

# first time = 0
# second time total = 0 + 5
# third time total = 5 + 10
# fourth time total = 15 + 15
# fifth time total = 30 + 20 = 50


new_numbers = list(range(1, 261))
# this credits a list pof number from 1 to 260
#challenge: sum up all the numbers from 1 to 260
#and print ther total


new_numbers = list(range(1, 261))
# this creates a list of numbers from 1 to 260

total = 0

for number in new_numbers:
    total += number   # add each number to the total

print(total)  # print the final total


print("total zum from 1 to 260 is:", total)
