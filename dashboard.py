import streamlit as st #biblioteca pra criar dashboards
import pandas as pd #biblioteca pra manipular dados
import plotly.express as px #biblioteca pra criar gráficos interativos

st.set_page_config(layout='wide') #configuração da página

# 01: Como uma visao mensal
#faturamento por unidade
#tipo de produrto mais vendido
#contribuição por filial 
#como estao avaliações das filiais


df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',') #carrega os dados de vendas
df['Date'] = pd.to_datetime(df['Date']) #converte a coluna Date para datetime
df=df.sort_values('Date') #ordena o dataframe pela data 

st.title('Dashboard de Vendas do Supermercado') #título do dashboard
st.subheader('Visão Mensal') #subtítulo do dashboard

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month)) #cria uma nova coluna com o mês e ano
month = st.sidebar.selectbox('Selecione o Mês', df['Month'].unique()) #cria um seletor de mês
df_month = df[df['Month'] == month] #filtra o dataframe pelo mês selecionado

#fitro

df_filtered = df[df['Month'] == month]

# colunas para os indicadores 
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Indicadores

fig_date = px.bar(df_filtered, x='Date', y='Total', color="City", title='Faturamento Diário')
col1.plotly_chart(fig_date)

fig_date = px.bar(df_filtered, x='Date', y='', 
                  color="City", title='Faturamento Diário')
col1.plotly_chart(fig_date)