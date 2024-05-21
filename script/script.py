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

total_bugs = df['qtda_bugs'].sum()

correct_bugs_average = df['bugs_corrigidos'].mean()

total_done_chores = df['tarefas_concluidas'].sum()

average_diary_tasks_done = df['tarefas_concluidas'].mean()

df['produtividade_diaria'] = df['tarefas_concluidas'] / df['horas_trabalhadas']

print(f"Total de Horas Trabalhadas: {hours_worked}")
print(f"Média Diária de Horas Trabalhadas: {media_diaria_horas_trabalhadas:.2f}")
print(f"Total de Bugs Corrigidos: {total_bugs_corrigidos}")
print(f"Total de Bugs Que Deveriam Ser Corrigidos: {total_bugs}")
print(f"Média Diária de Bugs Corrigidos: {correct_bugs_average:.2f}")
print(f"Total de Tarefas Concluídas: {total_done_chores}")
print(f"Média Diária de Tarefas Concluídas: {average_diary_tasks_done:.2f}")

ultima_semana = df[df['semana'] == df['semana'].max()]


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

#gráficos em barra, são os mais utilizados. 
#Indicam, geralmente, um dado quantitativo sobre diferentes variáveis, lugares ou setores e não dependem de proporções. 
#Os dados são indicados na posição vertical, enquanto as divisões qualitativas apresentam-se na posição horizontal.

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
