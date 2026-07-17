"""
   check if a number is even or odd
"""
def even():
    n  = 7
    if n %2 == 0:
        return "even"
    return "odd"

print(even())

"""
find the largest of the three numbers
3,9,2
"""

def largest():
    a,b,c = 3,9,2
    return max(a,b,c)
print(largest())

"""
Reverse a string

hello
"""

def  reverse():
    s = "hello"
    return s[::-1]

print(reverse())

def palindrom():
    s = "madam"
    return s == s[::-1]

print(palindrom())