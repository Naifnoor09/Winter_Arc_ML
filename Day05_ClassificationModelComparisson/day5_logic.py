"""
list_a = [1, 2, 3, 4], list_b = [3, 4, 5, 6]
Output: [3, 4] (Without using set()).
"""


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

list_u = list_a + list_b
print("Universal list : ",list_u)

seen = []
result = []

for i in list_u:
    if i in seen:
        result.append(i)
    else:
        seen.append(i)

print("Result : ",result)
    


