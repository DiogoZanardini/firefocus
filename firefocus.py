
import streamlit as st

from PIL import Image

st.title("Aplicação para previsão de incendios no Brasil.")

image = Image.open('img/logo.jpg')
st.image(image, caption='FIRE FOCUS PREDICTER V1.0.0 @2022')


st.markdown("Este é um Data App utilizado para exibir a solução de Inteligencia artificial para analise de possíveis focos de incêndio no Brasil.Este modelo preditivo está calibrado para aferir previsões aceitaveis até o mes de dezembro de 2022 ")


st.markdown("Para visualizar as previsões, selecione o período:")

 
meses = ('Maio','Junho',
        'Julho','Agosto','Setembro',
        'Outubro','Novembro','Dezembro')

col1, col2 = st.columns(2)

m_start = col1.selectbox('Mes inicial:', meses, index=0)

m_end   = col2.selectbox('Mes final:', meses, index=1)

btn = st.button('REALISAR PREVISÃO')

if btn:
    st.markdown('Vai pega fogo bagaray...')


