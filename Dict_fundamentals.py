# Method 1 - declare a Dict
num = {1: 'this ', 2: 'is method 1'}
print(num)
###################################################
# Method 2 - declare a Dict
dict0 = {}
dict0[1] = 'this'
dict0[2] = 'is method 2'
print(dict0)
###################################################
# Method 3
dict3 = dict([(1, "this "), (2, "is method 3")])
print(dict3)
###################################################
# Method 4 - FromKeys
list1 = [1, 2, 3, 4]
n = 0
my_dict = dict.fromkeys(list1, n)
print(my_dict)
###################################################
# Method 5  - Fromkeys range
dict1 = {}.fromkeys(range(1, 5), 4)
print(dict1)

###################################################
#  call individual key
print(num.get(1))
###################################################
# call all keys
print(dict.keys(num))
###################################################
# call all values
print(dict.values(num))
###################################################
# copy dict
numbers = dict(num)
print(numbers)
###################################################
# length
print(len(num))
###################################################
# delete
del num[2]
print(num)
###################################################
# In operation
print(2 in num)
###################################################
# insert a new value
num[2] = "two"
print(num)
###################################################
# update a value
num[2] = 2
print(num)

###################################################
# setdefault
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color", "White")
car.setdefault("country")
print(car)

