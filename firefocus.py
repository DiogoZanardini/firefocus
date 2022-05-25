

import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import statsmodels.api as sm


x = pd.read_csv('focos_mensal.csv')

model=sm.tsa.statespace.SARIMAX(x['total'],order=(0, 0, 2),
                                  seasonal_order=(1, 1, 2, 12))
results = model.fit()

col1, col2 = st.columns(2)
image = Image.open('img/logo.jpg')
col1.image(image, width= 70,caption='FFP v1.0.0')
image = Image.open('img/title.jpg')
col2.image(image)
st.markdown("Este é um Data App utilizado para exibir a solução de Inteligencia artificial para analise de possíveis focos de incêndio no Brasil. Este modelo preditivo está calibrado para aferir previsões aceitaveis até o mes de dezembro de 2022 ")
st.markdown("Para visualizar as previsões, selecione o período:")


meses_num = (53,54,55,56,57,58,59,60)

meses = ('Maio','Junho',
        'Julho','Agosto','Setembro',
        'Outubro','Novembro','Dezembro')

col1, col2 = st.columns(2)
m_start = col1.selectbox('Mes inicial:', meses[:-1], index=0)
m_start_index = meses.index(m_start)
m_end   = col2.selectbox('Mes final:', meses[m_start_index+1:], index=0)

m_start_num = meses_num[meses.index(m_start)]
m_end_num   = meses_num[meses.index(m_end)]

btn1 = st.button('REALIZAR PREVISÃO')
btn2 = st.button('LIMPAR')

if btn1:
    
    a = results.predict(start = m_start_num,
                        end   = m_end_num)

    fig = plt.figure(figsize=(14,6))
    x['total'].plot()
    a.plot()
    st.pyplot(fig) 

if btn2:
    st.markdown('')
   
