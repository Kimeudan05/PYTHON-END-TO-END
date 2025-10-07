# python data structures
#### 1. LISTS (they are ordered and changeable, allow duplicate members)

names = ["alice", "bob", "charlie","charlie"]
print(names)
print(len(names)) # length of list
print(names[0]) # first item
print(names[-1]) # last item
names[0] = "alex" # change item
names.append("david") # add item
names.insert(1, "eve") # insert item at specific position
names2 = ["frank", "grace"]
names.extend(names2) # extend list with another list
names.remove("charlie") # remove item
names.pop(2) # remove item at index
del names[0] # delete item at index
names.sort(reverse=True) # sort list
# names.clear() # clear list

# looping through a list
for name in names:
    print(name)
# OR by using index
for i in range(len(names)):
    print(names[i])
print(names)
##### LIST COMPREHENSION #####
squares = [x**2 for x in range(10)] # list of squares from 0 to 9
print(squares)

new_names = [name.upper() for name in names if len(name) > 3] # names with more than 3 letters in uppercase
print(new_names)

# sorting lists (by how close to 50)
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# overwrite the default (uppercase are sorted first)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

#reverse the order (first becomes last)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy list
list1 = names.copy() #using copy() method
list2 = list(names) #using list() function

# NB - to copy a list, do not use list2 = names as it will only create a reference to the original list

#join two lists
list3 = list1 + list2 # using + operator
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)

# using extend() method
list1.extend(list2)
print(list1)


#### 2. tuples (they are ordered and unchangeable, allow duplicate members)
thistuple = ("apple", "banana", "cherry", "cherry")
print(thistuple)
print(len(thistuple)) # length of tuple
print(thistuple[0]) # first item
print(thistuple[-1]) # last item
# thistuple[0] = "orange" # this will raise an error as tuples are immutable
# but we can convert it to a list, change it and convert it back to a tuple
y = list(thistuple)
y[0] = "orange"
thistuple = tuple(y)
print(thistuple)
# del thistuple # delete tuple

#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(app,*ban) = fruits # using * to assign the rest of the values to a variable

# tuple methods
print(thistuple.count("cherry")) # count occurrences of an item
print(thistuple.index("banana")) # index of an item

#### 3. sets (they are unordered, unchangeable*, and unindexed, no duplicate members)
# * sets are unchangeable, but we can add new items

myset = {"apple", "banana", "cherry", "apple"}
print(myset)
print(len(myset)) # length of set
# myset[0] = "orange" # this will raise an error as sets are
# but we can add new items
myset.add("orange") # add item
myset.update(["mango", "grape"]) # add multiple items
myset.remove("banana") # remove item, raises error if item not found
myset.discard("banana") # remove item, does not raise error if item not found
# myset.pop() # remove random item
# del myset # delete set
myset.clear() # clear set

# join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # using union() method (|)
set3 = set1 | set2 # using | operator
set3 = set1.intersection(set2) # items present in both sets (&)

# Frozen sets (same as sets except that you cannot add or remove items)
x= frozenset({"masila","jane","mukilo"})


###### 4 DICTIONARIES ### (changeable,unordered ,no dupliactes)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
brand = car.get("brand")
brand2 = car["brand"]
car.update({"year":2020})
for key,value in car.items():
    print(f"{key} => {value}")
car["price"]= 5564
# car.pop("year")
# del car["year"]
# del car # deletes the whole dict
# car.clear # clear the dictionary

# nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# accessing nested dictionaries
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])