import pandas as pd

df = pd.DataFrame({'Funcionario' : ["Joao", "Maria", "Pedro"],
                   'Banco de horas' : [2, 30, 7],
                   'Tarefas pendentes' : [2, 1, 6],
                   'Salario' : [500, 700, 600],
                   'Cargo' : ["Desenvolvedor", "CEO", "Analista"]})

print (df.dtypes)

print (df.columns)

input()