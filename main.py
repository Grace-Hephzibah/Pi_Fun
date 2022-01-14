import pi

size = int(input("Enter the number of digits you want to see in pi : \n"))
check = 0

for i in pi.pi:
    if check == size-1:
        break

    if check % 100 == 0 and check != 0:
        print()

    if i == ' ' or i == '\n':
        continue

    print(i, end="")
    check += 1
