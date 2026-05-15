temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

salas_riscos_maiores = {
        "numeros_salas": [],
        "maior_registro_encontrado": 0
}

salaAtual = 0
soma = 0
registro_critico_atual = 0
media = 0


for sala in temperaturas:

    for temperatura in sala:
        soma += temperatura

        if temperatura >= 33:
            registro_critico_atual += 1

    if salas_riscos_maiores["maior_registro_encontrado"] == registro_critico_atual:
        salas_riscos_maiores["numeros_salas"].append(salaAtual + 1)

    elif registro_critico_atual > salas_riscos_maiores["maior_registro_encontrado"]:
        salas_riscos_maiores["numeros_salas"].clear()
        salas_riscos_maiores["numeros_salas"].append(salaAtual + 1)
        salas_riscos_maiores["maior_registro_encontrado"] = registro_critico_atual

    media = soma / len(sala)

    print(f"Sala {salaAtual+1}")
    print(f"Media: {media:.2f}")
    print(f"Registros criticos: {registro_critico_atual}")
    print()

    salaAtual += 1
    media = 0
    soma = 0
    registro_critico_atual = 0

print()

if len(salas_riscos_maiores["numeros_salas"]) > 1:
    salas_str = [str(sala) for sala in salas_riscos_maiores["numeros_salas"]]
    print(f"Salas com maior risco: Salas {', '.join(salas_str)}")
else:
    print(f"Sala com maior risco: Sala {salas_riscos_maiores["numeros_salas"][0]}")
