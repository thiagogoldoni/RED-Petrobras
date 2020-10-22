def calculo_pagamento_imp (funcionario, horas_trabalhadas, valor_hora):
    horas = int (horas_trabalhadas)
    valor = int (valor_hora)
    
    if horas <= 40:
        salario = horas * valor
    else:
        extra = horas - 40
        salario = 40 * valor + (extra * 2 * valor)
    
    print ("Salario do(a)", funcionario, " = R$", salario)


calculo_pagamento_imp("Joao", 40, 50)
calculo_pagamento_imp("Maria", 50, 55)

input()