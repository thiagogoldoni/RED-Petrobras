import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Funcionario' : ["Joao", "Maria", "Pedro"],
                   'Banco de horas' : [2, 30, 7],
                   'Tarefas pendentes' : [2, 1, 6],
                   'Salario' : [500, 700, 600],
                   'Cargo' : ["Desenvolvedor", "CEO", "Analista"]})

df.plot(x = 'Funcionario', y = 'Salario', kind = 'bar')
plt.show()

input()