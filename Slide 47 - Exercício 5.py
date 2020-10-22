salario = float( input("Digite o salario atual: ")) 

if salario <= 1250:
    novo = salario + (salario * (15/100))
else:
    novo = salario + (salario * (10/100))
    
print ("Quem ganhava R$", salario, "agora vai ganhar R$", novo)


input()