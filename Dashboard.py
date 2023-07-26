import pickle as pk
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


import src.plots as pl
import src.plotSerie as pls
import src.dataframes as df


def main():
    st.set_page_config(
        page_title  ="Real-Time Data Science Dashboard",
        layout      ="wide",
    )
    st.title('Dashboard evasão universitária')
    tab1,tab2  = st.tabs(['Dashboard Main','Serie Historica'])

    with tab1: Tab1()
    with tab2: Tab2()





def Tab1():
    col1, col2 = st.columns([0.6,0.6])
    with col1:
        Unidade = col1.selectbox(
            label   = 'Unidade',
            options = df.Unidades(),
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
        col1.plotly_chart(
            pl.PiePlotIgressoDesistencia(
                df.TotalDeEvasaoPorUnidadeModalidade(Unidade,Ano)
            )
        )

    with col2:
        col2.plotly_chart(
            pl.PiePlotGeneroDesistencia(
                df.TotalDeEvasaoPorUnidadeGenero(Unidade,Ano)
                )
        )    


def Tab2():
    Unidade = st.checkbox('Por Unidade')

    if (Unidade):
        Unidades = st.multiselect('Selecione',options =df.Unidades())
        
        st.plotly_chart(
            pls.LinePlotSerieEvasãoPorUnidade(
                df.SerieEvasaoHistoricaPorUnidade(),
                Unidades
            )
        )
        st.plotly_chart(
            pls.SerieEvasãoCursoTotais(df.SerieTotalDeEvasaoPorUnidade(Unidades))
        )
    else:
     
        st.plotly_chart(
            pls.LinePlotSerieEvasãoSerieHistorica(
                df.SerieEvasãoHistorica()
            )   
        )
        print(df.SerieTotalDeEvasaoPorUnidade(df.Unidades()))
        st.table(df.SerieTotalDeEvasaoPorUnidade(df.Unidades()))
        
            
            
if __name__ == '__main__':
    main()