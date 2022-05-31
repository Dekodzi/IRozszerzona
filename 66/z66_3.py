def sol(f):
    was_right = False
    last_set = str()
    answer = []
    for line in f:
        line = line.strip()
        line_list = line.split()
        a = int(line_list[0])
        b = int(line_list[1])
        c = int(line_list[2])
        if (c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2) and not was_right:
            was_right = True
            last_set = line
        elif (c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2) and was_right:
            temp = [last_set, line]
            answer.append(temp)
            last_set = line
        else:
            was_right = False
            last_set = str()
    return answer


file = open("trojki.txt", 'r')

print(sol(file))

file.close()