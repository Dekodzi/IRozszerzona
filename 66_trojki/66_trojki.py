def zad_1(file):
    for line in file:
        print(line)
    return 0


def zad_2(file):
    for line in file:
        line = line.split()
        print(line)
    return 0


def zad_3(file):
    for line in file:
        suma = 0
        line = line.split()
        for eline in line:
            suma += int(eline)
        print(suma)
    return 0


def zad_3_2(file):
    for line in file:
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        suma = a + b + c
        print(suma)
    return 0


def zad_4(file):
    counter = 0
    for line in file:
        suma = 0
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        suma = a + b
        if suma > c:
            print(line)
            counter += 1
    print("tych linijek jest: ", counter)
    return 0


def zad_5(file):
    for line in file:
        line = line.split()
        sum = 0
        a = line[0]
        for i in a:
            sum += int(i)
        b = line[1]
        for i in b:
            sum += int(i)
        c = int(line[2])
        if sum == c:
            print(line)
    return 0

file = open("66_trojki", "r")

file.close()
