def sol(f):
    sequences = []
    numbers = []
    for line in f:
        line = line.strip()
        number = int(line, 2)
        if is_halfprime(number):
            sequences.append(line)
            numbers.append(number)
    return len(sequences), max(numbers), min(numbers)


def is_halfprime(n):
    if len(factorise(n)) == 2:
        return True
    else:
        return False

def factorise(n):
    factors = []
    for i in range(2, n):
        while n % i == 0:
            n //= i
            factors.append(i)
    return factors


file = open("ciagi.txt", 'r')

print(sol(file))

file.close()