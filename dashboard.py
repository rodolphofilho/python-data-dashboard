import streamlit as st          # Biblioteca para criar app web interativo
import pandas as pd            # Biblioteca para manipular dados (tabelas)
import plotly.express as px    # Biblioteca para criar gráficos interativos

st.set_page_config(layout="wide")  # Deixa a página em modo tela cheia (larga)

# Lê o arquivo CSV com separador ; e decimal ,
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Converte a coluna Date para formato de data
df["Date"] = pd.to_datetime(df["Date"])

# Ordena os dados pela data
df = df.sort_values("Date")

# Cria uma nova coluna com Ano-Mês (ex: 2024-1)
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Cria um filtro na barra lateral para escolher o mês
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Filtra o dataframe pelo mês selecionado
df_filtered = df[df["Month"] == month]

# Cria 2 colunas na primeira linha
col1, col2 = st.columns(2)

# Cria 3 colunas na segunda linha
col3, col4, col5 = st.columns(3)

# Gráfico de barras: faturamento por dia e por cidade
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", 
                  title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Gráfico de barras horizontal: faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Agrupa por cidade e soma o faturamento
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()

# Gráfico de barras: faturamento por filial
fig_city = px.bar(city_total, x="City", y="Total",
                  title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Gráfico de pizza: faturamento por forma de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Agrupa por cidade e calcula a média das avaliações
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()

# Gráfico de barras: avaliação média por filial
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                    title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
