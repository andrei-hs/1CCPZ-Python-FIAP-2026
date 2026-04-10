def print_lyrics():
    print("Never gonna give you up")
    print("Never gonna let you down")
    print("")

print_lyrics()

def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem-vindo(a)!")

nome_digitado = str(input("Digite seu nome: "))
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado = soma(1,5)
print(resultado)
print(type(resultado))
