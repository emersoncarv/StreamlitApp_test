import streamlit as st

st.header("Resumo dos Dados")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregados")
else:
    dados = st.session_state['dados'].describe().reset_index()
    st.write(dados)

    # análise de N itens
    top_n = st.session_state.get('top_n', 10)
    dados_brutos = dados
    dados = dados_brutos.head(top_n)
    st.write(dados)
