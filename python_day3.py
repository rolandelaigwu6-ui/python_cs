"""
Learning list
lesson:  unpacking List Items
         Slicing Items from a List

"""

lst = ['item1','item2','item3','item4','item5']
first_item, second_item, third_item, *rest = lst
# print(first_item)
# print(second_item)
# print(third_item)
print(rest)

# Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]


print(all_fruits)
print(orange_mango_lemon)
print(orange_and_lemon)
