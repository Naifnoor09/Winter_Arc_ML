"""
The Challenge :

- Create this list: numbers = [10, 15, 20, 25, 30]
- Write a for loop that creates a new list called squared_numbers.
- Inside the loop, square the number (x * x).

BUT: Only add it to the list if the original number is even (divisible by 2).
Print the result.

(Expected Output: [100, 400, 900])

"""

number = [10, 15, 20, 25, 30]
squared_numbers = []

for n in number :
    if n%2 == 0:
        sq = n*n
        squared_numbers.append(sq)
    
print(squared_numbers)


