def sol(f):
    amount = 0
    differences = []
    for line in f:
        line = line.split()
        if len(line) == 1:
            pass
        else:
            if is_arithmetic(line):
                amount += 1
                d = int(line[1]) - int(line[0])
                differences.append(d)
    return [amount, max(differences)]


def is_arithmetic(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        a = int(sequence[i])
        b = int(sequence[i+1])
        d = b-a
        differences.append(d)
        for j in differences:
            if d != j:
                return False
    return True


file = open("ciagi.txt", 'r')
ans = open("wynik1.txt", 'w')

out = sol(file)
ans.write(str(out))

file.close()
ans.close()
