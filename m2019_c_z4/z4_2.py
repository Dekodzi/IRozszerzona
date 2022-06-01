def sol(f):
    numbers = []
    for line in f:
        line = line.strip()
        num = int(line)
        back_num = int(line[::-1])
        if is_prime(back_num):
            numbers.append(num)
    return numbers


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


file = open("pierwsze.txt", 'r')
save = open("wyniki4_2.txt", 'w')

out = sol(file)
for i in out:
    temp = str(i) + '\n'
    save.write(temp)

file.close()
save.close()
