def sol(f):
    numbers = []
    for line in f:
        line = line.strip()
        line_list = line.split()
        a = int(line_list[0])
        b = int(line_list[1])
        c = int(line_list[2])
        if is_prime(a) and is_prime(b) and a*b == c:
            numbers.append(line)
    return numbers


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


file = open("trojki.txt", 'r')

print(sol(file))

file.close()