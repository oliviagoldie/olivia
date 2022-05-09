animals = ["bird", "fox", "cat", "rat", "alligator"]

animals.append("giraffe")

moreAnimals = ["monkey", "ant eater", "red panda"]


animals.extend(moreAnimals)

animals.insert(4, "snake")

animals.pop(3)

animals.remove("snake")

del animals[2]

del animals

for counter in animals:
    print(counter)