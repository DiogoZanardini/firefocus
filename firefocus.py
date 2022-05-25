import streamlit as st

from PIL import Image

col1, col2 = st.columns(2)

image = Image.open('img/logo.jpg')

col1.image(image, width= 150,caption='FIRE FOCUS PREDICTER V1.0.0 @2022')

col2.title("Previsão de incendios")



st.markdown("Este é um Data App utilizado para exibir a solução de Inteligencia artificial para analise de possíveis focos de incêndio no Brasil. Este modelo preditivo está calibrado para aferir previsões aceitaveis até o mes de dezembro de 2022 ")

st.markdown("Para visualizar as previsões, selecione o período:")

meses = ('Maio','Junho',
        'Julho','Agosto','Setembro',
        'Outubro','Novembro','Dezembro')

col1, col2 = st.columns(2)

m_start = col1.selectbox('Mes inicial:', meses[:-1], index=0)

m_start_index = meses.index(m_start)

m_end   = col2.selectbox('Mes final:', meses[m_start_index+1:], index=0)


btn1 = st.button('REALIZAR PREVISÃO')
btn2 = st.button('LIMPAR')

if btn1:
    x = st.markdown('Vai pega fogo bagaray...')

if btn2:
    x = st.markdown('')


