def sol(f):
    numbers = []
    for line in f:
        line = line.strip()
        num = int(line)
        if is_prime(num) and num >= 100 and num <= 5000:
            numbers.append(line)
    return numbers


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


file = open("liczby.txt", 'r')
save = open("wyniki4_1.txt", 'w')

out = sol(file)
for i in out:
    temp = str(i) + '\n'
    save.write(temp)

file.close()
save.close()
