<h1>Relatório de Progresso - Do Something Design</h1>
Este projeto tem a finalidade de organizar e estruturar dados brutos para obter insights sobre a produtividade dos funcionários de uma empresa de desenvolvimento de software. A "Do Something Design" foi contratada para avaliar a produtividade de uma equipe de engenheiros de software. Davi, um dos funcionários da nossa empresa, conversou com a equipe e conseguiu os dados referentes à produtividade da equipe para realizar a análise.

## Objetivo do Projeto
O objetivo deste relatório é demonstrar a importância da análise dos dados de um projeto de desenvolvimento de software ao longo de uma semana. Os dados fornecidos permitirão ao proprietário da equipe de desenvolvimento obter insights sobre o progresso do projeto, identificar possíveis áreas de melhoria e tomar decisões informadas para garantir o sucesso do projeto.

## Requisitos
Para a elaboração deste relatório, foram considerados os seguintes requisitos:

Utilizar Jupyter Notebook ou Google Colab: Para realizar a análise de dados e gerar visualizações.
Realizar análise exploratória: Explorar os dados para entender padrões e tendências.
Responder cada uma das perguntas com a visualização mais adequada: Usar gráficos e tabelas para apresentar os resultados.
Organização do notebook: O notebook deve estar organizado, com descrições do passo a passo da análise em markdown, apresentação dos resultados e insights gerados.
Itens do Relatório

## Itens do Relatório

O relatório de progresso diário incluirá os seguintes itens:

- **Total de Horas Trabalhadas**: Soma das horas trabalhadas pela equipe em cada dia.
- **Média Diária de Horas Trabalhadas**: Média de horas trabalhadas por dia.
- **Total de Bugs Corrigidos**: Soma dos bugs corrigidos em cada dia.
- **Média Diária de Bugs Corrigidos**: Média de bugs corrigidos por dia.
- **Total de Tarefas Concluídas**: Soma das tarefas concluídas em cada dia.
- **Média Diária de Tarefas Concluídas**: Média de tarefas concluídas por dia.
- **Produtividade Diária**: Tarefas concluídas por hora trabalhada.


## Existem 2 formas de usar

<h4>Primeira forma de usar(A mais fácil)</h4>
Abre esse link: https://colab.research.google.com/drive/1u2q_Uw7tuuO_UjNFg-4U0ws31uxKmQpI?usp=sharing
Em caso de erro, considere essas soluções:

- **Os dados não aparecem**: Você precisa baixar os dados.csv contido na pasta dados desse repositório, anexar dados.csv na pasta do google colab e atualizar o endereço da variável dados
```python
dados = pd.read_csv('endereço do arquivo csv que você colocou na pasta do google colab'```)
