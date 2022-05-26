def sol(f1, f2):
    same_numbers_amount = 0
    f1_greater_f2_amount = 0
    for i in range(0, 1000):
        num_1 = int(f1.readline().strip(), 8)
        num_2 = int(f2.readline().strip())
        if num_1 == num_2:
            same_numbers_amount += 1
        elif num_1 > num_2:
            f1_greater_f2_amount += 1
    return same_numbers_amount, f1_greater_f2_amount


file_1 = open("liczby1.txt", 'r')
file_2 = open("liczby2.txt", 'r')

print(sol(file_1, file_2))

file_1.close()
file_2.close()
