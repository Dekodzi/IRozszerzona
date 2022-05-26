def sol(f):
    min = None
    max = None
    for line in f:
        line = line.strip()
        number = int(line, 8)
        if min == None:
            min = line
        if max == None:
            max = line
        if int(min, 8) > number:
            min = line
        elif int(max, 8) < number:
            max = line
    return min, max


file_1 = open("liczby1.txt", 'r')

print(sol(file_1))

file_1.close()