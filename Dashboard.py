import pickle as pk
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


import src.plots as pl
import src.dataframes as df


def main():
    st.set_page_config(
        page_title  ="Real-Time Data Science Dashboard",
        layout      ="wide",
    )
    st.title('Dashboard evasão universitária')
    
    col1, col2 = st.columns([0.6,0.6])

    with col1:
        Unidade = col1.selectbox(
            label   = 'Unidade',
            options = df.Localidades(),
        )

        Genero = col1.checkbox(label='Por gễnero')

    with col2:
        Ano  = col2.select_slider(
            label   = 'Ano de saidas',
            options = [ano for ano in range(1998,2024)]
        )   


    col1 ,col2 = st.columns([2,0.8])

    with col1:
        if (not(Genero)):
            col1.plotly_chart(
                pl.BarplotDesistenciaAlunos(
                    df.TotalDeEvasaoPorUnidade(Unidade,Ano)
                    )
                )
        else: 
            col1.plotly_chart(
                pl.BarplotDesistenciaGenero(
                    df.TotalDeEvasaoPorUnidadeGenero(Unidade,Ano)
                    )
                )
    with col2:
        col2.plotly_chart(
            pl.PiePlotGeneroDesistencia(
                df.TotalDeEvasaoPorUnidadeGenero(Unidade,Ano)
                )
        )    


            
            
if __name__ == '__main__':
    main()