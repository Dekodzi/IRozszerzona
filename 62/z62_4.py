def sol(f):
    amount_of_six_dec = 0
    amount_of_six_oct = 0
    for line in f:
        line = line.strip()
        line_oct = str(oct(int(line)))
        for i in line:
            if i == '6':
                amount_of_six_dec += 1
        for i in line_oct:
            if i == '6':
                amount_of_six_oct += 1
    return amount_of_six_dec, amount_of_six_oct


file_1 = open("liczby2.txt", 'r')

print(sol(file_1))

file_1.close()