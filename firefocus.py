import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import statsmodels.api as sm

meses = ('Maio','Junho',
        'Julho','Agosto','Setembro',
        'Outubro','Novembro','Dezembro')

x = pd.read_csv('focos_mensal.csv')
x.index = pd.DatetimeIndex(x['dia'])

model=sm.tsa.statespace.SARIMAX(x['total'],order=(0, 0, 2),
                                  seasonal_order=(1, 1, 2, 12))
results = model.fit()

col1, col2= st.columns((1,4))

image = Image.open('img/logo.jpg')
col1.image(image, width= 70,caption='FFP v1.0.0')
image = Image.open('img/title.jpg')
col2.image(image)
col2.markdown("Este é um Data App utilizado para exibir a solução de Inteligencia artificial para analise de possíveis focos de incêndio no Brasil. Este modelo preditivo está calibrado para aferir previsões aceitaveis até o mes de dezembro de 2022 ")
st.subheader("Para selecionar o período, deslise os botões abaixo:")

m_start, m_end = st.select_slider('',options=meses, value=('Maio','Dezembro'))
m_start_num    = meses.index(m_start)+52
m_end_num      = meses.index(m_end)+52

spacer, col1, spacer = st.columns((5,40,1))
col1.write(f'{m_start} até {m_end}')

col1, col2 = st.columns((4,1))
    
a = results.predict(start = m_start_num, end = m_end_num)
fig, ax = plt.subplots(figsize=(15,6))
plt.xlabel("\n Meses", size=28)
plt.ylabel("Total de focos por dia\n ", size=28)
ax.plot(a)
ax.scatter(a.index, a)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%y'))

plt.xticks(size=22)
plt.yticks(size=22)

col1.pyplot(fig)

z= pd.DataFrame(a)
z = z.rename(columns={"predicted_mean": "Focos"})
z.index = z.index.strftime('%b-%y')
z['Focos'] = round(z['Focos']).astype(int)
col2.dataframe(z)




