# Find squares of numbers

nums = [i for i in range(1, 1000000)]

squares = []

for n in nums:
    squares.append(n ** 2)

print(len(squares))
#Optimized Code
# Find squares of numbers

squares = [n ** 2 for n in range(1, 1000000)]

print(len(squares))
#output
999999
#Explanation
The original program creates two lists:
1. nums
2. squares
The optimized program directly creates the squares list using list comprehension.
This removes the unnecessary nums list and makes the code shorter and more efficient.