c = int(input("ingresa el numero: "))
lista = [1, 3, 4, 7, 9, 10]
ok = False
izq = 0
der = len(lista)-1


while ok == False and izq < der:

    med = (izq+der) // 2

    if lista[med] == c:
        print("ese mismo es el numero")
        ok = True

    elif lista[med] < c:
        izq = med + 1

    else:
        der = med - 1

if not ok:
    print("ese no esta")
