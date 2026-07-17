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

def fibonacci():
    n = 5
    a,b = [0,1]
    for i in range(n):
        print(a)
        new_sum = a+b
        a = b
        b = new_sum
    return new_sum

print(fibonacci())

def sec_largest():
    lst = [2,6,8,3]
    count = 0
    for i in lst:
        for s in range(3): 
          if i > 0:
            i[s] += count[s]
    return count

print(sec_largest())