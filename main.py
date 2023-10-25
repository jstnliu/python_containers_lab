# Exercise 1
# Create a list named students containing some student names (strings).

students = [
    {'name': 'Jimothy'},
    {'name': 'Gary'},
    {'name': 'Bryant'},
]

# Print out the second student’s name.

print(students[1])

# Print out the last student’s name.

print(students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.

foods = ('steak', 'pie', 'bacon')

# Use a for loop to print out the string “[food goes here] is a good food”.

for food in foods:
    print(f"{food} is a good food")


# Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods

short_foods = foods[1:]
for short_food in short_foods:
    print(short_food)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# “I was born in city, state - population of population”

my_hometown = {
    'city': 'Monterey Park',
    'state': 'California',
    'population': 'at least 12 people'
}
if 'city' in my_hometown:
    print(f"I was born in {my_hometown['city']}, {my_hometown['state']} - population of {my_hometown['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# “city = Arcadia”
# “state = California”
# “population = 58000”

for key, value in my_hometown.items():
    print(f"{key} of {value}")


# Exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student
# Within the for loop, add a dictionary to the cohort list that combines the student’s name and the food in the foods list at the same index. Each dictionary will have this shape:

#   {
#     'student': 'Tina',
#     'fav_food': 'Cheeseburger'
#   }

# Iterate over the cohort list, printing out each item (it’s not necessary to format the dictionaries).

cohort = []
students = [
    {'name': 'Jimothy'},
    {'name': 'Gary'},
    {'name': 'Bryant'},
]
foods = ('steak', 'pie', 'bacon')

for idx, student in enumerate(students):
    student_food = {
        'student': student['name'],
        'fav_food': foods[idx]
    }
    cohort.append(student_food)
for student_info in cohort:
    print(student_info)


# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

students = [
    {'name': 'Jimothy'},
    {'name': 'Gary'},
    {'name': 'Bryant'},
]

awesome_students = [print(f"{student['name']} is awesome!") for student in students]

# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.

foods = ('steak', 'pie', 'bacon')

a_foods = [print(food) for food in foods if 'a' in food]


