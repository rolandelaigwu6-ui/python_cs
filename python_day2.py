print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

"""
Let us start connecting the dots and start making use of what 
we already know to calculate (area, volume,density, weight, perimeter, distance, force).
"""
# Calculating area of a circle

raduis = 10
area_of_circle = 3.14 * raduis ** 2
print("Area of a circle:",area_of_circle)


# base =float(input("Enter Base: "))
# height = float(input("Enter Height: "))

# total = (base * height)/2
# print("the area of the triangle is ", total)


# a = int(input("side a: "))
# b = int(input("side b: "))
# c = int(input("side c"))
# d = a,b,c
# print(sum(d))

# length = float(input("enter the length: "))
# width = float(input("enter width: "))
# area = length*width
# print("area of a rectangle:",area )

sec = 60
inaday = 24
total = 24 * 60**2

days = 365
daysinyears = 365*100
number_of_sec_lived = daysinyears*total
print("numbers of seconds lived = ", number_of_sec_lived)

hour = 40
rate = 28
total_erning = hour*rate
print("total money earn", total_erning)
print(type('10') ==  type(10))
print(int(9.8) == 10)
print((7//3)== int(2.7))
print(7//3)
print(10%2==0)
print(11%2==0)
length = "python"
output = len((length))
print(float(output))
drag = "dragon"
pyt = "python"
if 'on' in drag and pyt:
    print("true")
else:
    print("false")