import pickle as pk
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import mysql.connector as mysql
from   streamlit_option_menu import option_menu

import crud as c
import plots as p



def main():
    st.set_page_config(layout="wide")
    with st.sidebar:
        selected = option_menu("Main Menu", ["Visualizar", 'Conexão'], 
                                icons=['house', 'gear'], 
                                menu_icon="cast", 
                                default_index=1)
        
    if (selected == "Visualizar"): visualizar()
    if (selected == "Conexão")   : conexao()  
        



def visualizar():
    st.title("UFC Desistancias")
    
    col1 , col2 = st.columns([1,1])
    with col1:
        ano_saida = st.selectbox('Ano de saida',[i for i in range(1972,2023)])

    with col2:
        nome_unidade = st.selectbox('Nome da Unidade',c.nome_unidade())

    tab1, tab2 , tab3 , tab4 = st.tabs(["📈 Plot", "📈Por genero","📈Anos","🗃 DataFrame"])
   

    with tab1:  
        dataframe = c.selecao(ano_saida,nome_unidade)

        if ( not(dataframe.empty) ):
            fig = p.grafico_1(dataframe)
            st.plotly_chart(fig,theme=None, use_container_width=True)       
        else:
            st.write('não possui dados') 
    

    with tab2:
        dataframes = c.por_sexo(ano_saida,nome_unidade)
        
        if ( not( dataframes[0].empty ) ):
            fig = p.grafico_2(dataframes)
            st.plotly_chart(fig,theme=None, use_container_width=True)
        else:
            st.write('não possui dados')


    with tab3:
        button = st.checkbox('Por Unidade de ensino')
        
        if (button):
            dataframes = [ c.por_ano_unidade(i) for i in c.nome_unidade() ]
            fig = p.grafico_4(dataframes)
            st.plotly_chart(fig,theme=None, use_container_width=True)
            
        else:
            dataframes = c.por_ano_geral() 
            fig = p.grafico_3(dataframes)
            st.plotly_chart(fig,theme=None, use_container_width=True)
     

    with tab4:
        st.dataframe(pd.read_sql('select * from dados_alunos;',c.conexao()))



def conexao():
   
    st.title('Conexão')
    with st.container():
        user = st.text_input('User :    ','root')
        pasw = st.text_input('Password: ')
        data = st.text_input('Database: ')
        button = st.button('Importar')
        
        if (button):
            file = open('conect.dat','wb')
            pk.dump([ user ,pasw ,data ],file,protocol=pk.HIGHEST_PROTOCOL)
            file.close()
            pd.read_csv('ufc.csv',sep=',').to_sql('dados_alunos', c.conexao(), if_exists='fail', index=False)
            
            
            
if __name__ == '__main__':
    main()