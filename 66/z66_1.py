def sol(f):
    numbers = []
    for line in f:
        line = line.strip()
        line_list = line.split()
        sum = 0
        for i in line_list[0]:
            sum += int(i)
        for i in line_list[1]:
            sum += int(i)
        if sum == int(line_list[2]):
            numbers.append(line)
    return numbers


file = open("trojki.txt", 'r')

print(sol(file))

file.close()