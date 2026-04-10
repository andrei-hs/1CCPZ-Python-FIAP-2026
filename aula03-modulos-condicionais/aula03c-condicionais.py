num = 15
num = num + 2
num /= 2
print(num)

print()

verifica_email = False
verifica_senha = True

login = verifica_email and verifica_senha

if login:
    print("Entrar no sistema")

if not login:
    print("Não entra aqui, senha errada >:-(")

print()

nota_final = 3

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
