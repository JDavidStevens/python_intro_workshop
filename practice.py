# # declare a variable
# x = 42
# print(f"x={x}")

# # numbers
# x = int(4)
# y = int('5')
# z = float(5)
# print(f"x = {x}, y={y}, & z={z}")

# # boolean types
# # True = 1 & False = 0
# x = True + False
# print(f"x={x}")

# # add number and string
# x = 3
# print(str(x)+" Three")
# # or
# y = 'three'
# print(int(x)+3)

# # functions
# def add(x, y=5):
#     print(x+y)


# add(5)
# add(7, 2)

# # list
names = ["Jimmy", "Kreashia", "Toree"]
# print(len(names))
# print(names[0])
names[2] = "Viktoriya"
# print(names)
# # doesn't modify list, just makes a copy:
# print(sorted(names, reverse=True))
# # modifies the underlying list:
# names.sort(reverse=True)
# print(f"reverse {names}")

# names.append("Heather")
names.insert(0, "Heather")
# print(names)

pets = ["Buddy"]
names.extend(pets)
# print("Buddy" in names)
# print("David" in names)
# print(f"1 {names}")
# names.remove("Buddy")
# names.pop()
names.pop(4)
# print(f"2 {names}")

# # TUPLES
# student = ("Kreashia", 12, "Theater", 3.8)
# print(student[2])
# name, age, subject, grade = student
# print(name)
# student = "Jimmy", 14, "History", 3.5
# print(type(student))

# # SETS
# dirt_bikes = {"Yamaha", "Suzuki", "Honda", "Kawasaki"}
# # print("KTM" in dirt_bikes)
# dirt_bikes.discard("Kawasaki")
# dirt_bikes.add("Kawasaki")

# bicycles = {"Diamondback"}
# dirt_bikes.update(bicycles)
# print(dirt_bikes)

# DICTIONARIES
child = {"name": "Toree", "age": 8, "hobby": "roller-blading", "girl": True}
# print(child.get("name"))
# print(child.items())
# print(child.keys())
# print(child.values())

child["siblings"] = ["Jimmy", "Kreashia"]
# print(child)

# # BOOLEANS
a = 0
b = 1
# print(a and b)

# LOOPS
clothes = ['pants', 'shirt', 'socks', 'shoes']

# for item in clothes:
#     print(item)
# for index, item in enumerate(clothes):
#     print(f"Item: {item} is at index: {index}")

# for x, y in child.items():
#     print(x, y)

# if 5 > 3:
# print("Go 5!")


def compare(a, b):
    if a < b:
        print("Go a!")
    elif a == b:
        print("Tie!")
    else:
        print("Go b!")


compare(7, 7)
