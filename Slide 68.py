def calculo_pagamento (horas_trabalhadas, valor_hora):
    horas = int (horas_trabalhadas)
    valor = int (valor_hora)
    
    if horas <= 40:
        salario = horas * valor
    else:
        extra = horas - 40
        salario = 40 * valor + (extra * 2 * valor)
    
    return salario

salario_joao = calculo_pagamento(40, 50)
salario_maria = calculo_pagamento(50, 55)

print ("O sal�rio do Jo�o � R$", salario_joao)
print ("O sal�rio da Maria � R$", salario_maria)


input()