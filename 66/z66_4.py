def sol(f):
    amount = 0
    lengths = []
    temp = []
    for line in f:
        line = line.strip()
        line_list = line.split()
        a = int(line_list[0])
        b = int(line_list[1])
        c = int(line_list[2])
        if is_triangle(a, b, c):
            amount += 1
            temp.append(line)
        else:
            lengths.append(len(temp))
            temp = []
    return [amount, max(lengths)]


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


file = open("trojki.txt", 'r')

print(sol(file))

file.close()