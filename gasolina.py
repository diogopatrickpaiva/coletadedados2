
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

grafico = sns.lineplot(x='dia', y='venda', data=df, marker='o', label='Preço da Gasolina')

plt.title('Variação do Preço da Gasolina ao Longo dos Dias', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço da Gasolina (R$)', fontsize=14)
plt.legend(title='Legenda')
plt.grid(True)

plt.savefig('gasolina.png')
plt.show()
