import streamlit as st

st.header("Resumo dos Dados")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregados")
else:
    # dados = st.session_state['dados'].describe().reset_index()
    # st.write(dados)

    top_n = st.session_state.get('top_n', 10)
    dados_brutos = st.session_state['dados']
    dados = dados_brutos.head(top_n)

    st.write('Dados Completos')
    st.write(dados_brutos.describe().reset_index())
    
    # análise de N itens
    st.write(f'Primeiros {top_n} itens')
    st.write(dados.describe().reset_index())
