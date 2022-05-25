def sol(f):
    amount = 0
    for line in f:
        line = line.strip()
        is_good = True
        was_1 = False
        for i in line:
            if i == '1' and not was_1:
                was_1 = True
            elif i == '1' and was_1:
                is_good = False
            else:
                was_1 = False
        if is_good:
            amount += 1

    return amount


file = open("ciagi.txt", 'r')

print(sol(file))

file.close()