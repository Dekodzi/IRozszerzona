def sol(f):
    first_terms = []
    lengths = []
    sequence = []
    for line in f:
        line = line.strip()
        if len(sequence) == 0:
            sequence.append(line)
        else:
            if int(sequence[-1]) <= int(line):
                sequence.append(line)
            else:
                first_terms.append(sequence[0])
                lengths.append(len(sequence))
                sequence = [line]
    longest = max(lengths)
    i = lengths.index(longest)
    return first_terms[i], longest


file_1 = open("liczby2.txt", 'r')

print(sol(file_1))

file_1.close()