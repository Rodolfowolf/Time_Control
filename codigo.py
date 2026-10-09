#Resources

# pip install streamlit
# pip install pandas
# pip install plotly


# tituleo - Sistema de Vendas
# Secao cadastrar vendas
    # campo data
    # Campo vendedor
    # campo produto
    # Campo quantidade
    # Campo valor
    # Botao cadastrar vendas
        # quando clicar no botao = adicionar a venda na tabela
# Secao vendas cadastradas
    #Tabela com as vendas
# secao dashboard
    #card/metrica = faturamento total
    #grafico de barra = venda por vendedor
    #grafico de pizza = venda por produto
    
import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
hour_control = pd.read_csv("Hour control.csv")

st.write("# Time Control System")

# secao de cadastro de vendas
st.sidebar.write("### Time Control Input")

day = st.sidebar.date_input("Worked Day")
address = st.sidebar.text_input("Address")
start_time = st.sidebar.number_input("Start Time", min_value=0, max_value=23, step=1)
finish_time = st.sidebar.number_input("Finish Time", min_value=0, max_value=23, step=1)
total = finish_time - start_time
Submit = st.sidebar.button("Submit Worked Hours")

# logica de cadastro de vendas
if Submit:
    new_day = [day, address, start_time, finish_time, total]
    last_line = len(hour_control)
    hour_control.loc[last_line] = new_day
    hour_control.to_csv("Hour control.csv", index=False)
    st.success("New day added!")


# secao de visualizar as horas trabalhadas
st.write("### Worked Hours Informed")
st.dataframe(hour_control)


# secao do dashboard
st.write("### Dashboard")
#card/metrica = total worked hours
total = hour_control["Total"].sum()
st.metric("Total Worked Hours", f"{total} hours")

#grafico de pizza = venda por produto
grafico1 = px.pie(hour_control, names="Address", values="Total", title="Worked Hours by Address")
st.plotly_chart(grafico1)

#grafico de barra = venda por vendedor
grafico2 = px.bar(hour_control, x="Address", y="Total", title="Worked Hours by Address")
st.plotly_chart(grafico2)

