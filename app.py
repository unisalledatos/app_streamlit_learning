import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import wooldridge as wd

st.set_page_config(layout='wide')
df = px.data.iris()
wage = wd.data('wage1') 
st.title("Ayuda con streamlit")

# Display

# text elements

tab1, tab2, tab3 = st.tabs(['tab1', 'tab2', 'tab3'])

with tab1:
    st.header("Esto es un header")

    st.divider()

    st.subheader("Esto es un subheader")

    st.divider()

    st.code(
    '''def hello():
        print("Hello, Streamlit!")''', language='python')

    st.divider()

    st.latex("y=\\textbf{X}\\beta + u")

    st.divider()

    # data elements

    st.dataframe(df)

    st.table(df.head())

    st.metric("Métrica", 10, 5)
    st.metric("Métrica 2", 10, -3)

    # chart elements
    fig, ax = plt.subplots(1, 1)
    ax.scatter(df['sepal_length'], df['petal_length'])
    st.pyplot(fig)

    fig = px.scatter(data_frame=df, 
                    x='sepal_length', 
                    y='petal_length', 
                    symbol='species_id',
                    hover_name='species_id')
    st.plotly_chart(fig)

    # input widgets

    if st.button("Clic aquí"):
        st.write("Has hecho clic")
        



    if st.toggle("Esto es un toggle"):
        fig = px.scatter(data_frame=df,
                        x='sepal_length',
                        y='petal_length',
                        color='species_id',
                        color_continuous_scale=['yellow', 'purple', 'grey'])
        st.plotly_chart(fig)
with tab2:
    gender = st.selectbox("Seleccione el género", wage['female'].unique())
    educ = st.slider("Seleccione años educación", 
                     wage['educ'].min(), 
                     wage['educ'].max())
    exper = st.select_slider("Seleccione años de experiencia", sorted(wage['exper'].unique()))
    filtro = wage[(wage['female'] == gender)&
                  (wage['educ'] == educ) & 
                  (wage['exper'] == exper)]
    st.dataframe(filtro)

    fig = px.scatter(data_frame=filtro,
                     x='educ',
                     y='wage',
                     color='married',
                     marginal_x='violin',
                     marginal_y='box')
    st.plotly_chart(fig)

with tab3:
    st.info("Ingresa cualquier texto")
    texto = st.text_input("Escribe el texto aquí: ")
    
    if len(texto) < 10:
        st.error("Demasiado corto")
    elif len(texto) == 10:
        st.success("Logrado")
    else:
        st.warning("Demasiado largo")


# layouts and containers

st.sidebar.write("Tenemos una barra al costado")

if st.sidebar.button("Clic aquí", key=2):
    st.sidebar.snow()
