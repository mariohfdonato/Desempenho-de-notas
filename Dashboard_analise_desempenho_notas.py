import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

tb_total = pd.read_csv('analise_desempenho_alunos_2024.CSV', sep=';')
soma = tb_total[['av_mensal','av_bimestral', 'simulado','trabalho','participacao']].sum(axis=1).copy()
#tb_media_bimestre = tb_total[['aluno','classe','bimestre']]
tb_total['media_bimestre'] = soma

st.title('Análise das notas dos alunos do ensino médio na disciplina de Física em três bimestres')

st.write('Neste Dashboard Interativo exploro alguns aspectos do desempenho dos alunos do ensino médio do Colégio Poligenes de Jaboticabal - SP em três bimestres. Em particular, comparo a distribuição de notas dos alunos (e suas parcelas: Avaliação Bimestral, Avaliação Mensal, Simulado, Trabalho e Participação) no Bimesrtre 1 e nos Bimestres 2 e 3 (em associação). Como houve a troca do professor de Física pouco antes da metade do Bimestre 2 (29-05-2024), a comparação anterior mostra como essa mudança afetou o desempenho dos alunos.')




#st.write('seletor de turma: 1 2 3 ou todos')

turma_num = {'Todas' : 0 , '1o Ano' : 1 , '2o Ano' : 2 , '3o Ano' : 3 }
bimestre_num = {'Todos' : 0, 'Bimestre 1': 1, 'Bimestre 2': 2, 'Bimestre 3': 3}
nota_col = {'Nota total': 'media_bimestre' , 'Avaliação Mensal' : 'av_mensal', 'Avaliação Bimestral' : 'av_bimestral', 'Simulado' : 'simulado','Trabalho':'trabalho','Participação':'participacao'}


col1, col2, col3 = st.columns(3)

#with col2:



#aba_histograma, aba_cumulativo, aba_sobreoautor = st.selectbox('Tipo de Gráfico', ['Histograma', 'Distribuição cumulativa'])

#col1, col2, col3 = st.columns(3)

##with col1:
#    st.header('Histograma da Nota Total nos 3 bimestres')
    
#    fig,ax = plt.subplots(figsize = (10,5))
#    ax = sns.histplot(tb_media_bimestre['media_bimestre'], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability')
#    plt.ylim((0,0.35))
#    st.pyplot(fig, use_container_width = True)

with col1:
        st.header('Selecione a turma, o bimestre, a parcela da nota e o tipo de gráfico')
        turma = st.selectbox('Turma', ['Todas', '1o Ano', '2o Ano','3o Ano'])
        bimestre = st.selectbox('Bimestre', ['Todos', 'Bimestre 1', 'Bimestre 2','Bimestre 3'])
        tipo_nota = st.selectbox('Parcela da nota', ['Nota total', 'Avaliação Bimestral', 'Avaliação Mensal','Simulado','Trabalho', 'Participação'])
        tipo_grafico = st.selectbox('Tipo de Gráfico', [ 'Histograma', 'Distribuição Cumulativa' ] )
        st.write('Peso das notas:')
        st.write('Avaliação Bimestral - 3, Avaliação Mensal - 2, Simulado - 3, Trabalho - 1, Participação - 1.')
        #st.write('Gráfico com a dispersão de notas em todos os bimestres')
    
        fig1, ax1 = plt.subplots(figsize = (10,5))
        if (turma_num[turma]!=0) & (bimestre_num[bimestre]!=0):
            ax1 = sns.histplot(tb_total[ (tb_total['classe']==turma_num[turma]) & (tb_total['bimestre']==bimestre_num[bimestre])][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax1.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para o {turma} do ensino médio no {bimestre}')
            ax1.set_ylabel('Frequência normalizada')
            ax1.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig1, use_container_width = True)
        elif (turma_num[turma]==0) & (bimestre_num[bimestre]!=0):
            ax1 = sns.histplot(tb_total[ tb_total['bimestre']==bimestre_num[bimestre] ][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax1.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para todas as turmas do ensino médio no {bimestre}')
            ax1.set_ylabel('Frequência normalizada')
            ax1.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig1, use_container_width = True)
        elif (turma_num[turma]!=0) & (bimestre_num[bimestre]==0):
            ax1 = sns.histplot(tb_total[ tb_total['classe']==turma_num[turma] ][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax1.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para o {turma} do ensino médio nos 3 bimestres')
            ax1.set_ylabel('Frequência normalizada')
            ax1.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig1, use_container_width = True)
        else:
            ax1 = sns.histplot(tb_total[nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax1.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para o todas as turmas do ensino médio nos 3 bimestres')
            ax1.set_ylabel('Frequência normalizada')
            ax1.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig1, use_container_width = True)
    
with col2:
        st.header('Comparação das notas antes e depois da troca de professor')
        #st.write('A troca de professor aconteceu pouco antes da metade do segundo bimestre (29-05-2024)')
        st.subheader('Antes da troca')
    
        fig2, ax2 = plt.subplots(figsize = (10,5))
        if (turma_num[turma]!=0):
            ax2 = sns.histplot(tb_total[ (tb_total['classe']==turma_num[turma]) & (tb_total['bimestre']==1)][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax2.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para o {turma} do ensino médio no Bimestre 1')
            ax2.set_ylabel('Frequência normalizada')
            ax2.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig2, use_container_width = True)
        else:
            ax2 = sns.histplot(tb_total[ tb_total['bimestre']==1 ][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax2.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para todas as turmas do ensino médio no Bimestre 1')
            ax2.set_ylabel('Frequência normalizada')
            ax2.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig2, use_container_width = True)

        st.subheader('Depois da troca')
        fig3, ax3 = plt.subplots(figsize = (10,5))
        if (turma_num[turma]!=0):
            ax3 = sns.histplot(tb_total[ (tb_total['classe']==turma_num[turma]) & (tb_total['bimestre']!=1)][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax3.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para o {turma} do ensino médio nos Bimestres 2 e 3')
            ax3.set_ylabel('Frequência normalizada')
            ax3.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig3, use_container_width = True)
        else:
            ax3 = sns.histplot(tb_total[ tb_total['bimestre']!=1 ][nota_col[tipo_nota]], binrange=(0,10), binwidth=0.3, kde = True, stat = 'probability', cumulative = (tipo_grafico=='Distribuição Cumulativa'))
            ax3.set_title(f'{tipo_grafico} das notas de(a) {tipo_nota} para todas as turmas do ensino médio nos Bimestres 2 e 3')
            ax3.set_ylabel('Frequência normalizada')
            ax3.set_xlabel(f'{tipo_nota}')
            #plt.ylim((0,0.35))
            st.pyplot(fig3, use_container_width = True)

with col3:
        st.header('Comentários gerais')
        st.write('Do ponto de vista geral, em termos de desempenho de notas, a troca de professor foi positiva para as turmas. Isso fica evidenciado na distribuição da Nota Total dos alunos, que anteriormente era estreita e com pico um pouco abaixo de 6 (a média de aprovação para este colégio) e passa a ser mais larga com seu pico mais próximo de 7, com alunos atingindo notas mais altas (acima de 8) em fração considerável (de ~ 0% para ~ 20%). Em termos de relacionamento com o professor e qualidade de aulas, todas as turmas relataram melhora considerável nesses dois aspectos e destacaram a formação mais adequada do professor, o domínio dos assuntos abordados e uma melhor comunicação professor-aluno no dia-a-dia da sala de aula.')
        st.write('Com base no que relata o novo professor da disciplina, além dos motivos destacados pelos alunos, ele atribui a melhora das notas também à elaboraração de avaliações mais adequadas para a realidade e conhecimento dos alunos, ajustando e aumentando o nível de dificuldade dos exercícios com o tempo e à medida que as maiores dificuldades relatadas pelos alunos eram trabalhadas.')

        if turma=='1o Ano':
            st.header('Comentários acerca do 1o Ano')
            st.write('Sobre as características do 1o Ano do ensino médio, o professor relata que essa é uma classe que, em geral, possui interesse na disciplina de Física, mas que encontravam dificuldades até mesmo nos conceitos mais simples. Ele destaca que teve que trabalhar novamente alguns assuntos antes de poder dar continuidade com o cronograma, mas que agora ele é capaz de seguir com as aulas normalmente.')

        if turma=='2o Ano':
            st.header('Comentários acerca do 2o Ano')
            st.write('Sobre as características do 2o Ano do ensino médio, o professor relata que essa é uma classe que, em geral, apesar de possuir uma boa capacidade de entendimento dos assuntos tratados na disciplina de Física, tem muito pouco interesse em todas as disciplinas (como também relatado por outros professores do colégio). Isto é uma presente dificuldade para o professor. Ele relata que, diferente das outras turmas, o desempenho de notas nesta sala melhorou, mas não de forma tão significativa.')

        if turma=='3o Ano':
            st.header('Comentários acerca do 3o Ano')
            st.write('Sobre as características do 3o Ano do ensino médio, o professor relata que essa é uma classe que, em geral, possuia pouco interesse na disciplina de Física, encontrava dificuldades em alguns conceitos, mas que desenvolveram interesse na disciplina com o decorrer do tempo. Ele destaca que teve que trabalhar a revisão de alguns assuntos antes de poder dar continuidade com o cronograma, mas que agora ele é capaz de seguir com as aulas normalmente e enxerga com otimismo o desempenho dos alunos nas provas de vestibular.')
    
    
    
    

    
#st.header('Conclusões')
#st.write('Comentário a a a a a a a a a a a a aa a a a a a a a a a a a a aa a  a a aa a a a  a a a a a a aaaaa aa  aa aa a a a a a a  a a a aaaa a aa aa a aaaa a')