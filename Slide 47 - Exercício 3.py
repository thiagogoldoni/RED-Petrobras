distancia = int( input ("Digite a distância da sua viagem: "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia *0.45
    
print ("O preço da sua passagem é R$", preco)


input()