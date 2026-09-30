lista = [52, 33, 9.5, True, "Python"]
valor = 0
contador = 1


while contador <= 3:
    valor = input("Insira um valor: ")
    lista.append(valor)
    contador = contador + 1

for item in lista:
    tipo = type(item)
    print(f"{item} is of the data type {tipo}")