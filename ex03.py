frase = input("Digite uma frase: ")

cont = {}

for char in frase:
    if char in cont:
        cont[char] += 1
    else:
        cont[char] = 1

print("Quantos caracteres tem na frase: ")
for char, quantidade in cont.items():
    print("Caractere '{}' repete {} vezes".format(char, quantidade))
