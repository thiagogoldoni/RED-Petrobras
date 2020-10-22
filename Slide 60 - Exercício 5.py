sexo = input ("Digite seu sexo (M ou F): ")
while sexo not in "MmFf":
    sexo = input ("Dados inválidos. Por favor, informe seu sexo: ")
    
print ("Sexo", sexo, "registrado com sucesso")

input()