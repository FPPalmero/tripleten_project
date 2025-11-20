import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('data/vehicles.csv')

st.header('Análise de dados de carros usados')


select_chart = st.selectbox(
    'Selecione o tipo de gráfico',
    ('Selecione um gráfico',
     'Histograma de Odômetro',
     'Histograma de Dias Listados por Condição',
     'Histograma de Ano do Modelo por Preço',
     'Dispersão de Odômetro por Preço'))


if select_chart == 'Histograma de Odômetro':
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(df, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


elif select_chart == 'Dispersão de Odômetro por Preço':
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.scatter(df, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)


elif select_chart == 'Histograma de Ano do Modelo por Preço':
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(df, x="model_year", y="price")

    st.plotly_chart(fig, use_container_width=True)


elif select_chart == 'Histograma de Dias Listados por Condição':
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(df, x="days_listed", color="condition", opacity=0.7)

    st.plotly_chart(fig, use_container_width=True)
