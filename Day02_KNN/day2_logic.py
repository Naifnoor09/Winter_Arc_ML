"""
Write a function called check_palindrome(word).

Logic:
- It takes a string input (e.g., "madam" or "hello").
- It returns True if the word is the same forward and backward.
- It returns False otherwise.

Test it: print(check_palindrome("racecar")) should print True.

Constraint: Do not use word[::-1] (The Python cheat code). 

Try to write the logic using a loop or comparing indices. (If you get stuck, use the cheat code, but try the hard way first).
"""

def check_palindrome(word):
    lenght = len(word)
    for i in range(0,lenght//2):
        if word[i] != word[lenght-1-i]:
            return False
    return True
    
word = input("Enter a word : ")
result = check_palindrome(word)
print(result)
    
