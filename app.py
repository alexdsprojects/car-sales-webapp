import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar el título y estilo de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Análisis Interactivo de Anuncios de Vehículos</h1>", unsafe_allow_html=True)
st.markdown("Explora los datos de anuncios de venta de autos con gráficos interactivos. Selecciona las visualizaciones que deseas ver a continuación:", unsafe_allow_html=True)

# Leer el dataset
df = pd.read_csv('vehicles_us.csv')

# Crear columnas para una mejor disposición
col1, col2 = st.columns(2)

# Checkbox para cada gráfico
with col1:
    show_histogram = st.checkbox("Histograma del Odómetro", value=False)
    show_scatter = st.checkbox("Dispersión: Precio vs Odómetro", value=False)

with col2:
    show_bar = st.checkbox("Barras: Tipos de Vehículos", value=False)
    show_box = st.checkbox("Caja: Precios por Condición", value=False)

# Gráfico 1: Histograma del Odómetro
if show_histogram:
    st.markdown("### Distribución del Odómetro")
    st.write("Este histograma muestra cómo se distribuyen los valores del odómetro entre los vehículos. Puedes observar si hay un rango típico de kilometraje en los anuncios.")
    fig_hist = px.histogram(df, x="odometer", title="Distribución del Odómetro", 
                            color_discrete_sequence=["#3498DB"], nbins=50)
    fig_hist.update_layout(bargap=0.2)
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico 2: Dispersión de Precio vs Odómetro
if show_scatter:
    st.markdown("### Relación entre Precio y Odómetro")
    st.write("Este gráfico de dispersión muestra la relación entre el precio de los vehículos y su odómetro. Busca patrones: ¿los autos con más kilometraje son más baratos?")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs Odómetro",
                             color="condition", hover_data=["model", "model_year"],
                             color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico 3: Barras de Tipos de Vehículos
if show_bar:
    st.markdown("### Distribución por Tipo de Vehículo")
    st.write("Este gráfico de barras muestra cuántos vehículos hay de cada tipo (SUV, sedan, pickup, etc.). Es útil para ver qué categorías son más comunes en los anuncios.")
    fig_bar = px.bar(df, x="type", title="Conteo por Tipo de Vehículo",
                     color="type", color_discrete_sequence=px.colors.qualitative.Set2)
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico 4: Caja de Precios por Condición
if show_box:
    st.markdown("### Distribución de Precios por Condición")
    st.write("Este gráfico de caja muestra cómo varían los precios según la condición del vehículo (nuevo, bueno, justo, etc.). Observa los valores atípicos y las medianas.")
    fig_box = px.box(df, x="condition", y="price", title="Precios por Condición",
                     color="condition", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_box, use_container_width=True)

# Pie de página
st.markdown("<p style='text-align: center; color: #7F8C8D;'>Desarrollado por Alejandro Vásquez con Streamlit y Plotly Express</p>", unsafe_allow_html=True)