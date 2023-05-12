def eatmeals365():
    print("Eat breaky")
    print("Eat lunch")
    print("Eat dinner")
counter = 0
for day in range(1,8):
    print("Current day", day)
    eatmeals365()
    counter += 1
print("total:", counter)

def hw():
    print("Hello world")

counter = 0
for hello in range(1, 51):
    print(counter)
    hw()
    counter += 1
print(counter)
