set = {"name", "harry", "age", 32}
#sets are unchangable (once they're created, that's it, but you can add or remove items later)
#sets are unordered (you never know what order they'll appear once called, it changes unless specified with sort())
# 
dict = {"name": "harry", "age": "32"}
tuple = ("name", "harry", "age", [32])
list = ["name", "harry", "age", [32]]

print(type(set))
print(type(dict))
print(type(tuple))
print(type(list))

print(reversed(set))