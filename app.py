#Importación de las librerías necesarias
import pandas as pd
import plotly.graph_objects as go  #Importación de plotly.graph_objects como go
import streamlit as st

#Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Contenido de la aplicación Streamlit
st.title('Análisis de datos de anuncios de venta de coches')   

#Crear un botón: Construir histograma en la aplicación Streamlit
hist_button = st.button('Construir histograma')

#Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #Crear un histograma utilizando plotly.graph_objects
    #Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    #Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    #Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    #'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


#Crear un botón: Construir gráfico de dispersión en la aplicación Streamlit
scatter_button = st.button('Construir gráfico de dispersión')

#Lógica a ejecutar cuando se hace clic en el botón
if scatter_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para analizar la relacón entre el odometro (Kilometraje) vs el precio de venta del coche')

    #Crear un gráfico de dispersión (Scatter) utilizando plotly.graph_objects
    #Se crea una figura vacía y luego se añade un rastro de gráfico de dispersión
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    #Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio',
                      xaxis_title = 'Odómetro (Kilometraje)',
                      yaxis_title = 'Precio de venta del coche (USD)')

    #Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    #'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

