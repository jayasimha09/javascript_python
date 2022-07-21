# creating empty set.
from operator import index, indexOf


s = set()

# adding items to the list.
s.add(1)
s.add(3)
s.add(2)
s.add(4)
s.add(3)
print(s)

# removal of the set item.
s.remove(2)
print(s)

# finding length of the set item.
print(f"There are total of {len(s)} elements.")


# adding names to the set.
names = set()
names.add("python")
names.add("javascript")
names.add("java")
names.add("SQL")
print(names)