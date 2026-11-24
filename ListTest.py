friends = []
for i in range(10):
    name = input("Enter a friend's name: ")
    friends.append(name)

friends.sort()
friends.reverse()

extra_name = input("Enter an extra friend's name: ")
friends.append(extra_name)

print(friends)