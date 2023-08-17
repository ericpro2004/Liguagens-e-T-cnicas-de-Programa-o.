# Avaliação 2 LTP.

#1)
valor_inicial = float(input("Digite o valor para ser recebido o desconto: "))
desconto = float(input("Digite o valor do desconto: "))

print(f"O valor inicial é {valor_inicial}, o desconto é de {desconto}% e o valor final é {valor_inicial - valor_inicial/100 * desconto}.")

#2)
peso = float(input("Digite o seu peso para calcular seu imc: "))
altura = float(input("Digite sua altura: "))

print(f"O seu Indice de massa corporal é {peso/altura**2}")

#3)

#Tabela da verdade.
print("Tabela da verdade (Or, And e Not).")
print("---------------------------------")
print(True, 'ou', True, "=", True or True)
print(True, 'ou', False, "=", True or False)
print(False, 'ou', True, "=", False or True)
print(False, 'ou', True, "=", False or False)
print("---------------------------------")
print(True, "e", True, "=", True and True)
print(True, "e", False, "=", True and False)
print(False, "e", True, "=", False and True)
print(False, "e", True, "=", False and False)
print("---------------------------------")
print(True, "not", True, "=", not True)
print(True, "not", False, "=", not False)
print(False, "no", True, "=", not True)
print(False, "not", True, "=", not False)
print("---------------------------------")
