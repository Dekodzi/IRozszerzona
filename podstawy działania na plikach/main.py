#zadanie: wypisz linijki pliku
def ex_1(x):
    for line in x:
        print(line)
#zadanie: wypisz linijki pliku jako listy
def ex_2(x):
    for line in x:
        line = line.split()
        print(line)
#zadanie: wypisz sumę liczb z jednego wiersza
def ex_3(x):
    for line in x:
        line = line.split()
        suma = 0
        for i in line:
            suma += int(i)
        print(suma)
#zadanie: wypisz linie w których suma dwóch pierwszych 
#liczb jest większa od trzeciej liczby
def ex_4(x):
    counter = 0
    for line in x:
        line = line.split()
        suma = 0
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        suma = a+b
        if suma>c:
            print(line)
            counter +=1
    print(counter)
#zadanie: wypisz linie w których suma cyfr dwóch pierwszych liczb
#jest równa trzeciej liczbie
def ex_5(x):
    for line in x:
        line = line.split()
        sum_of_digits = 0
        a = line[0]
        for i in a:
            sum_of_digits += int(i)
        b = line[1]
        for i in b:
            sum_of_digits += int(i)
        c = int(line[2])
        if sum_of_digits == c:
            print(line)
#zadanie z gwiazdką: wypisz te linie w których dwie pierwsze liczby
#są liczbami pierwszymi oraz ich lioczyn jest równy trzeciej liczbie
def is_prime(num):
    prime = True
    for i in range(2, round(num**0.5)+1): #to jest wydajniejszy sposób ale bezpieczniej jest zrobić od 2 do num/2 + 1
        if num%i == 0:
            prime=False
    return prime

def ex_6(x):
    for line in x:
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        if is_prime(a) and is_prime(b) and a*b==c:
            print(line)

file = open("66_trojki.txt", 'r')

#ex_1(file)
#ex_2(file)
#ex_3(file)
#ex_4(file)
#ex_5(file)
#ex_6(file)

file.close()
