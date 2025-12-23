"""
Task: Count frequency of characters in a string:
"hello" -> {'h':1, 'e':1, 'l':2, 'o':1} without using Counter.
"""

word = input("Enter a word to find frequency of letters used : ")

freq = {}

for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
        
