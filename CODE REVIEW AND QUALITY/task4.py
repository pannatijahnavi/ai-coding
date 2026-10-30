students = ["Alice", "Bob", "Charlie"]

print("Welcome", students[0])
print("Welcome", students[1])
print("Welcome", students[2])
#Refactored Code
def welcome_students(students):
    for student in students:
        print("Welcome", student)


students = ["Alice", "Bob", "Charlie"]

welcome_students(students)
#output
Welcome Alice
Welcome Bob
Welcome Charlie
#Explanation
Instead of writing three separate print() statements, a function and a for loop are used.
This makes the program:
- Reusable
- Easier to maintain
- Shorter
- Suitable for any number of students