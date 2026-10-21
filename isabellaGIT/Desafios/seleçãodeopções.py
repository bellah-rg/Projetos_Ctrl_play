print("-"*35)
print("    Sorveteria do Brás")
print("-"*35)

print()
print()

print("-" * 35)
print("    OPÇÕES")
print("-" * 35)

print()
print()

print(" 1 -> Morango")
print(" 2 -> Chocolate")
print(" 3 -> Baunilha")
print(" 4 -> Cereja")
print(" 5 -> Maracuja")

print("-" * 30)
print("    OPEÇÕES DE CORBETURA")
print("- * 30")
print(" 6 -> caramelo")
print(" 7 -> morango ")
print(" 8 -> chocolate")
print(" 9 -> uva")
print(" 10 -> limão")
print(" 11 -> maracuja")

print()
print()

escolhaSorvete = input("Digete um sabor:")

escolhaSabor = input("Digite um sabor:")


if escolhaSorvete == "1":
    print("Usuário escolheu sabor Morango")
elif escolhaSorvete == "2":
    print("Usuário escolheu sabor Chocolate")
elif escolhaSorvete == "3":
    print("Usuário escolheu sabor Baunilha")
elif escolhaSorvete == "4":
    print("Usuário escolheu sabor Cereja")
elif escolhaSorvete == "5":
    print("Usuário escolheu sabor Maracuja")
else:
    print("Usuário escolheu sabor ***inválido***.")
