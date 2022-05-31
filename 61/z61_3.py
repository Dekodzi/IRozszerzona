def sol(f):
    errors = []
    for line in f:
        line = line.split()
        if len(line) == 1:
            pass
        else:
            differences = []
            for i in range(len(line)-1):
                d = int(line[i+1]) - int(line[i])
                differences.append(d)
            proper_diff = 0
            i = 0
            while proper_diff == 0:
                if differences[i] == differences[i+1]:
                    proper_diff = differences[i]
                else:
                    i += 1
            if i == 0:
                first = int(line[0])

    return errors


file = open("bledne.txt", 'r')
ans = open("wynik3.txt", 'w')

sol(file)

#out = sol(file)
#for i in out:
#    line = str(i) + '\n'
#    ans.write(line)

file.close()
ans.close()
