def sol(f):
    sequences = []
    for line in f:
        line = line.strip()
        n = len(line) // 2
        if len(line) % 2 == 0:
            w1 = line[:n]
            w2 = line[n:]
            if w1 == w2:
                sequences.append(line)
    return len(sequences)


file = open("ciagi.txt", 'r')

print(sol(file))

file.close()