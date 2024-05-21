# -*- coding: utf-8 -*-
"""trabalho_individual_resilia.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OHgbKKyiZ90ZYDNzIaG-REnwQm-Pwxwa

# <font color="pink"> Do Something Design
 ## relatório de produtividade
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('/content/dados/dados.csv')

df = pd.DataFrame(dados)

sns.set(style="whitegrid")


hours_worked = df['horas_trabalhadas'].sum()


media_diaria_horas_trabalhadas = df['horas_trabalhadas'].mean()

total_bugs_corrigidos = df['bugs_corrigidos'].sum()

correct_bugs_average = df['bugs_corrigidos'].mean()

total_bugs = df['qtda_bugs'].sum()

total_done_chores = df['tarefas_concluidas'].sum()

average_diary_tasks_done = df['tarefas_concluidas'].mean()

df['produtividade_diaria'] = df['tarefas_concluidas'] / df['horas_trabalhadas']

"""
###A equipe está trabalhando mais do que o normal, mas os bugs não estão sendo corrigidos devidamente,
####Temos um total de 179 horas totais trabalhadas que não parecem estarem bem feitas, não são todas as horas produtivas, esse tempo total é parcialmente produtivo"""

print(f"Total de Horas Trabalhadas: {hours_worked}")

"""###A produtividade em Bugs é mais em relação ao dia do que a quantidade de funcionários
####Os bugs resolvidos são variados não relacionados a quantas pessoas, então alguma pessoa ou forma de resolver é alterada no meio da semana, ou alguma atividade torna as pessoas mais produtividas

"""

print(f"Total de Bugs Corrigidos: {total_bugs_corrigidos}")

"""###A média das horas não parece corresponder a produtividade esperada
####Como visto no primeiro ponto, esse daqui é mais uma informação que a equipe trabalha de tal forma, mas não gera o resultado esperado, o tempo focado que a equipe passa parece ser pouco, pois se o tempo médio é 6 horas e alguns minutos, então além do tempo está sendo mal alocado a equipe pode estar sendo mal utilizada, de forma que alguns funcionários podem acabar trabalhando pouco e corrigindo muitos bugs ou podem trabalhar pouco e não corrigir a quantidade esperada de bugs e trabalho feito

"""

print(f"Média Diária de Horas Trabalhadas: {media_diaria_horas_trabalhadas:.2f}")

"""###Trabalho feito em dia não apopriado
####Levando em conta que a empresa não trabalha aos fins de semana, is trabalhos estão sendo empurrados para sábado, significando que temos parte do trabalho feito para tal tempo, deixado para depois, indicando uma má organização das tarefas, talvez o gestor ou quem administra essas tarefas não está fazendo um bom trabalho.
"""

plt.subplot(1, 1, 1)
sns.barplot(x='dia', y='bugs_corrigidos', data=df)
plt.title('Bugs Corrigidos por Dia')

plt.subplot(1, 1, 1)
sns.barplot(x='dia', y='tarefas_concluidas', data=df)
plt.title('Tarefas Concluídas por Dia')

"""###Ou seja, poderíamos ter mais bugs corrigidos
####O total de bugs corrigidos não foi tão grande, quanto deveria ser, aqui temos quantos bugs foram corridos
"""

print(f"Total de Bugs Corrigidos: {total_bugs_corrigidos}")

"""Aqui temos quantos bugs **deveriam** ter sido corrigidos

"""

print(f"Total de Bugs Que Deveriam Ser Corrigidos: {total_bugs}")

"""###Concluindo com o quanto de tarefa e bugs são feitos(concluidos)
###A empresa precisa investigar como as tarefas são dadas, a relação entre a equipe/gestor, equipe/tarefas, método que é feito das tarefas, método que é organizado as tarefas. Pela média é perceptível que poderia estar melhor, por mais que podesse mitigar dependendo da época, por exemplo, poderiamos passar por um momento em que o gestor não está bem de saúde, por isso as produtivadade não está tão boa.

"""

print(f"Média Diária de Bugs Corrigidos: {correct_bugs_average:.2f}")
print(f"Total de Tarefas Concluídas: {total_done_chores}")
print(f"Média Diária de Tarefas Concluídas: {average_diary_tasks_done:.2f}")

"""###Na última semana trabalharam mais
####Isso demonstra que pode ter tido algum aspecto entre essas semanas que fez a equipe trabalhar mais, também pode indicar que quando o prazo está apertando o time decide ser produtivo, o que pode tornar o trabalho a ser entregue mal feito, ter estresse e desentendimentos.
"""

resposta_1 = ultima_semana['horas_trabalhadas'].sum()
resposta_2 = ultima_semana['horas_trabalhadas'].mean()
resposta_3 = ultima_semana['bugs_corrigidos'].sum()
resposta_4 = ultima_semana['bugs_corrigidos'].mean()
resposta_5 = ultima_semana['tarefas_concluidas'].sum()
resposta_6 = ultima_semana['tarefas_concluidas'].mean()

print(f"Total de Horas Trabalhadas na última semana: {resposta_1}")
print(f"Média Diária de Horas Trabalhadas na última semana: {resposta_2:.2f}")
print(f"Total de Bugs Corrigidos na última semana: {resposta_3}")
print(f"Média Diária de Bugs Corrigidos na última semana: {resposta_4:.2f}")
print(f"Total de Tarefas Concluídas na última semana: {resposta_5}")
print(f"Média Diária de Tarefas Concluídas na última semana: {resposta_6:.2f}")
print(f"Quantidade de Bugs a serem resolvidos no final da última semana: {quantidade_bugs}")

"""###Graficar
####Analisando o gráfico geral, temos varianças, mas no final concluo que a equipe precisa de uma inovação no método de organização e produção, o gestor pode ser convidado para fazer algum curso ou workshop, isso poderá ajudar ele e a equipe a serem mais produtivos em mais fixos no trabalho.
"""

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.barplot(x='dia', y='horas_trabalhadas', data=df)
plt.title('Horas Trabalhadas por Dia')

plt.subplot(2, 2, 2)
sns.barplot(x='dia', y='bugs_corrigidos', data=df)
plt.title('Bugs Corrigidos por Dia')

plt.subplot(2, 2, 3)
sns.barplot(x='dia', y='tarefas_concluidas', data=df)
plt.title('Tarefas Concluídas por Dia')

plt.subplot(2, 2, 4)
sns.lineplot(x='dia', y='produtividade_diaria', data=df, marker='o')
plt.title('Produtividade Diária')

plt.tight_layout()
plt.show()