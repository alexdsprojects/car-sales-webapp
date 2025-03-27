import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataset
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de Anuncios de Venta de Autos")

# Botón para el histograma
hist_button = st.button("Mostrar Histograma del Odómetro")
if hist_button:
    st.write("Distribución de los valores del odómetro en el dataset")
    fig_hist = px.histogram(df, x="odometer", title="Histograma del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para el gráfico de dispersión
scatter_button = st.button("Mostrar Gráfico de Precio vs Odómetro")
if scatter_button:
    st.write("Relación entre el precio y el odómetro de los vehículos")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig_scatter, use_container_width=True)