set = {"name", "harry", "age", 32}
#sets are unchangable (once they're created, that's it, but you can add or remove items later)
#sets are unordered (you never know what order they'll appear once called, it random everytime)
#sets don't allow duplicates (if you have any duplicates in  the set, 1 of them will be removed once the set is called)

dict = {
    "name": "harry",
    "age": "32"
}
#dictionaries are ordered (once called, they appear as writen and you can refer to specific key:values)
#dictionaries are changable (can be changed, added or removed after it's be created)
#dictionaries don't allow duplicates

tuple = ("name", "harry", "age", [32])
#tuples are ordered
#tuples are unchangeable
#tuples allow duplicates

list = ["name", "harry", "age", 32]
#use [] to define a list
#lists are ordered
#lists are changeable
#lists allow duplicates
#lists pretty much print exactly what's written

print(type(set))
print(type(dict))
print(type(tuple))
print(type(list))

print(set)
#will come back rande=om each time
print(dict["name"])
#use [] to call the value of that key in the dict
print(tuple[0])
#square brackets [] call a specific index in the tuple (indexs start from 0)
print(list)