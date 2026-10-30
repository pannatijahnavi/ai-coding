# Calculate average score of a student
def calc_average(marks):

    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return avrage

marks = [85, 90, 78, 92]

print("Average Score is ", calc_average(marks)
#Errors Identified
1. avrage is a spelling mistake. It should be average.
2. The print() statement is missing a closing ).
#Corrected Code
# Calculate average score of a student
def calc_average(marks):
    total = 0

    for m in marks:
        total += m

    average = total / len(marks)
    return average


marks = [85, 90, 78, 92]

print("Average Score is", calc_average(marks))
#output
Average Score is 86.25
#Explanation
The program adds all the marks and divides the total by the number of marks.
