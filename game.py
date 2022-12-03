while True:
    pencils = input("How many pencils would you like to use:\n")
    if pencils.isdigit():
        pencils = int(pencils)
        if pencils > 0:
            break
        elif pencils <= 0:
            print("The number of pencils should be positive")
    else:
        print("The number of pencils should be numeric")

names = ["Jack", "John"]
while True:
    first = input("Who will be the first (John, Jack):\n")
    if first not in names:
        print("Choose between 'John' and 'Jack'")
    else:
        break

print("|" * pencils)
count = names.index(first)
taken_pencils = 1

while pencils > 0:
    while True:
        if  names[count % 2] == "Jack":
            print(f"{names[count % 2]}'s turn:")
            if pencils % 4 == 0:
                print("3")
                taken_pencils = 3
                break
            if pencils == 3:
                print("2")
                taken_pencils = 2
                break
            if pencils == 2:
                print("1")
                taken_pencils = 1
                break
            if pencils == 1:
                print("1")
                taken_pencils = 1
                break
            if pencils % 2 == 0:
                print("1")
                taken_pencils = 1
                break
            if pencils % 2 == 1:
                print("2")
                taken_pencils = 2
                break

        elif  names[count % 2] == "John":
            print(f"{names[count % 2]}'s turn!")
            taken_pencils = input()
            if taken_pencils.isdigit():
                taken_pencils = int(taken_pencils)
                if int(taken_pencils) not in range(1, 4):
                    print("Possible values: '1', '2' or '3'")
                    continue
                elif int(taken_pencils) > pencils:
                    print("Too many pencils were taken")
                    continue
                else:
                    break
            else:
                print("Possible values: '1', '2' or '3'")
                continue
    pencils -= taken_pencils
    count += 1
    if pencils != 0:
        print("|" * pencils)
print(f"{names[count % 2]} won!\n")