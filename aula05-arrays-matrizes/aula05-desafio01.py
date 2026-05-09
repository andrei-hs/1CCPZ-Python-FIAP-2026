# Me desafiei a não usar for
lista = ["Ana", "João", "Leo", "Bia"]

ponteiro1 = 0
ponteiro2 = 1
contador_dupla = 0

while(ponteiro1 != ponteiro2):
    contador_dupla = contador_dupla + 1
    print(f"Dupla {contador_dupla}: {lista[ponteiro1]} & {lista[ponteiro2]}")

    if ponteiro2 == (len(lista)-1) and (ponteiro1+1) < (len(lista)-1):
        ponteiro1 = ponteiro1 + 1
        ponteiro2 =  ponteiro1 + 1

    elif (ponteiro1+1) < (len(lista)-1):
        ponteiro2 = ponteiro2 + 1

    else:
        ponteiro1 = ponteiro1 + 1
