def sol(f):
    cubes = []
    for line in f:
        line = line.split()
        if len(line) == 1:
            pass
        else:
            temp = []
            for i in line:
                if is_cube(int(i)):
                    temp.append(int(i))
            if len(temp) != 0:
                cubes.append(max(temp))
    return cubes


def is_cube(n):
    for i in range(0, n+1):
        k = i**3
        if k == n:
            return True
        if k > n:
            return False


file = open("ciagi.txt", 'r')
ans = open("wynik2.txt", 'w')

out = sol(file)
for i in out:
    line = str(i) + '\n'
    ans.write(line)

file.close()
ans.close()
