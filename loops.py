fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print (fruit)
    print (fruit + "Pie")

# Prompt the user to input the number of students
num_students = int(input("Enter the number of students: "))

# Prompt the user to input the heights of each student
print("Enter the heights of the students (separated by spaces):")
student_heights = input().split()

# Convert the heights from strings to integers and calculate total height
total_height = 0
for i in range(num_students):
    height = int(student_heights[i])
    total_height += height

# Calculate the average height
average_height = round(total_height / num_students)

# Print the results
print(f"Total Height: {total_height}")
print(f"Number of students: {num_students}")
print(f"Average Height: {average_height}")

print("Enter the marks of the students (separated by spaces):")
student_scores = input().split()

# Convert the marks from strings to integers
for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

# Find the highest score
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print the highest score
print(f"The highest score in the class is: {highest_score}")

total = 0
for number in range(1,101):
    total += number
print (total)

for number in range(1,11,3):
    print(number)

target = int(input())
even_sum = 0
for number in range(2,target+1,2):
    even_sum += number
print (even_sum)

test = 100
for number in range(1,target+1):
    if number %3 == 0 and number % 5 == 0 :
        print ("FizzBuzz")
    elif number % 3 == 0 :
        print ("Fizz")
    elif number % 5 == 0 :
        print ("Buzz")
    else:
        print (number)

# end of for loops

