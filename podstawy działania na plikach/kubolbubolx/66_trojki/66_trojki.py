#1. wyswietl wszystkie linie z pliku 66_trojki.txt
def zad_1(file):
    for line in file:
        print(line)
    return 0


#2. wyswietl kazda linijke z pliku jako liste
def zad_2(file):
    for line in file:
        line = line.split()
        print(line)
    return 0


#3.wyswietl sume liczb w kazdej linice
def zad_3(file):
    for line in file:
        suma = 0
        line = line.split()
        for eline in line:
            suma += int(eline)
        print(suma)
    return 0


#3.wyswietl sume liczb w kazdej linice
def zad_3_2(file):
    for line in file:
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        suma = a + b + c
        print(suma)
    return 0


#4. wyswietl tylko te linijki z pliku, dla ktorych suma 
#liczb z pierwszej i drugiej kolumny jest wieksza trzeciej
#podaj ich ilosc
def zad_4(file):
    counter = 0
    for line in file:
        suma = 0
        line = line.split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        suma = a + b
        if suma > c:
            print(line)
            counter += 1
    print("tych linijek jest: ", counter)
    return 0


#5. wypisz wszytkie trojki liczb, w których suma cyfr dwóch 
#pierwszych liczb jest równa liczbie trzeciej
# 12 491 17         1+2+4+9+1=17
def zad_5(file):
    for line in file:
        line = line.split()
        sum = 0
        a = line[0]
        for i in a:
            sum += int(i)
        b = line[1]
        for i in b:
            sum += int(i)
        c = int(line[2])
        if sum == c:
            print(line)
    return 0

file = open("66_trojki", "r")

file.close()
