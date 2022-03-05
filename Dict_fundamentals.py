# Method 1 - declare a Dict
print("this is program1")
num = {1: 'this ', 2: 'is method 1'}
print(num)
print("###################################################")
# Method 2 - declare a Dict
print("this is program2")
dict0 = {}
dict0[1] = 'this'
dict0[2] = 'is method 2'
print(dict0)
print("###################################################")
# Method 3
print("this is program3")
dict3 = dict([(1, "this "), (2, "is method 3")])
print(dict3)
print("###################################################")
# Method 4 - FromKeys
print("this is program4")
list1 = [1, 2, 3, 4]
n = 0
my_dict = dict.fromkeys(list1, n)
print(my_dict)
print("###################################################")
# Method 5  - Fromkeys range
print("this is program5")
dict1 = {}.fromkeys(range(1, 5), 4)
print(dict1)
print("###################################################")
#  call individual key
print("this is program6")
print(num.get(1))
print("###################################################")
# call all keys
print("this is program7")
print(dict.keys(num))
print("###################################################")
# call all values
print("this is program8")
print(dict.values(num))
print("###################################################")
# copy dict
print("this is program9")
numbers = dict(num)
print(numbers)
print("###################################################")
# length
print("this is program10")
print(len(num))
print("###################################################")
# delete
print("this is program11")
num1 = {1: 'one', 2: 'two'}
del num1[2]
print(num1)
num2 = {1: '3', 2: '4'}
num2.pop(1)
print(num2)
print("###################################################")
# In operation
print("this is program12")
print(2 in num)
print("###################################################")
# insert a new value
print("this is program13")
num[2] = "two"
print(num)
print("###################################################")
# update a value
print("this is program14")
num[2] = 2
print(num)
print("###################################################")
# setdefault
print("this is program15")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.setdefault("color", "White")
car.setdefault("country")
print(car)
print("###################################################")
# update
print("this is program16")
dict4 = {1: 'one ', 2: 'two'}
dict5 = {3: 'three ', 4: 'four'}
print(dict4.update(dict5))
print(dict4)
print(dict5)

print("###################################################")