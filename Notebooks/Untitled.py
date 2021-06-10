#!/usr/bin/env python
# coding: utf-8

# # Tabela de Numero de viagens feitas por turistas 

# In[127]:


import matplotlib.pyplot as plt
import pandas as pd

#Associação do data frame ao csv em análise
dataframe_tur = pd.read_csv('N_viagens_de_ turistas_por_sexo_e_meio_de_transporte.csv')

dataframe_tur


# ## Ano mais recente em análise

# In[21]:


#função head lê os primeiros dados da tabela, neste caso, definimos que lia os primeiros 12
dataframe_tur.head(12)


# ## Ano mais antigo em análise

# In[22]:


#função tail lê os últimos dados da tabela, neste caso, definimos que lia os últimos 12
dataframe_tur.tail(12)


# ## Atribuir a variável principal

# In[23]:


#definimos a variável em análise principal - Número de viagens feitas por turistas - com a função set_index
dataframe_N_de_viagens = dataframe_tur.set_index(" N_de_viagens")

#utilizamos a função head para aparecer os 132 dados em análise
dataframe_N_de_viagens.head(132)


# ## Descubrir o mês de todos os anos com mais viagens realizadas

# In[122]:


#procuramos o mês com o máximo de variáveis realizadas através da função max, ao definirmos que o máximo em análise estava presente na variável N_de_viagens
total_list = dataframe_tur[' N_de_viagens'].tolist()

max_viagens = dataframe_tur[' N_de_viagens']== max(total_list)

dataframe_tur.loc[max_viagens]


# ## Responder à questão principal:
# ## Qual o mês do ano de 2020 em que houve mais viagens feitas por turistas?

# In[128]:


#Descubrir o máximo do ano de 2020 utilizando o id, que contrai-se entre 0 e 11 porque ao uilizar os meses, existe subreposição de tosos os anos
lista = dataframe_tur['Id']. between (1,12, inclusive=True)
total_list = dataframe_tur[lista]
numero = total_list[' N_de_viagens'].tolist()
meses = total_list['Id'].tolist()

#definimo o tipo de gráfico através da função plt.plot - gráfico de linha - tal como as suas caracteristicas
plt.plot(meses, numero, 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='-', linewidth=1)

#atribuimos nomes ao x e ao y, ao gráfico e definimos os intervalos do y
plt.xlabel('Meses de 2020')
plt.ylabel('Número de viagens')
plt.legend(loc='upper right')
plt.title('Viagens feitas por turistas mensalmente')
plt.xticks(meses)
plt.yticks([2000000, 4000000, 6000000])
plt.show()


# In[ ]:




