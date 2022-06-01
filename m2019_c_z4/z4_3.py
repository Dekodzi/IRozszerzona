def sol(f):
    count = 0
    for line in f:
        line = line.strip()
        num = int(line)
        while calculate_weight(num) >= 10:
            num = calculate_weight(num)
        if calculate_weight(num) == 1:
            count += 1
    return count


def calculate_weight(n):
    weight = 0
    number = str(n)
    for i in number:
        weight += int(i)
    return weight


file = open("pierwsze.txt", 'r')
save = open("wyniki4_3.txt", 'w')

out = str(sol(file))
save.write(out)

file.close()
save.close()
