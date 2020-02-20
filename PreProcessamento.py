import pandas as pd
base = pd.read_csv('credit-data.csv')
base.describe()

""" Localiza valores abaixo de 0 """

base.loc[base['age'] < 0 ]

""" Apagar a Coluna"""

base.drop('age', 1, inplace=True)
"""         |     |       |
            |     |       └─ Não Salvar em nenhuma variável o retorn
            |     └─ Vamos apagar 1 coluna
            └─ Qual coluna iremos apagar
"""

""" Apagar os registros com problema """

base.drop(base[base.age < 0].index, inplace = True)

""" Preencher os valores manualmente com a média"""

base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92
