import streamlit as st
from bs4 import BeautifulSoup

st.set_page_config(
    layout="wide",  # Define o layout da página como "wide" (amplo).
    page_icon="⚽",  # Define o ícone da página.
    page_title="Players",  # Define o título da página.
)

df_data = st.session_state["data"]

clubs = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubs)

df_data = df_data[(df_data["Club"] == club)]

players = df_data["Name"].unique()
player = st.sidebar.selectbox("Selecione um jogador", players)

players_stats = df_data[(df_data["Name"] == player)].iloc[0]

st.image(players_stats["Photo"])
st.title(players_stats["Name"])

st.markdown(f"**Clube:** {players_stats['Club']}")

# Limpar a posição usando BeautifulSoup
position_html = players_stats['Position']
soup = BeautifulSoup(position_html, "html.parser")
position_text = soup.get_text()

st.markdown(f"**Posição:** {position_text}")

col1, col2, col3, col4 =st.columns(4)
col1.markdown(f"**Idade:** {players_stats['Age']}")
col2.markdown(f"**Altura:** {players_stats['Height']}")
col3.markdown(f"**Peso:** {players_stats['Weight']}")
st.divider()

st.subheader(f"Overall: {players_stats['Overall']}")
st.progress(int(players_stats['Overall']))

col1, col2, col3, col4 =st.columns(4)
col1.metric(label="**Valor de Mercado**", value=f"${players_stats['Value']}")
col2.metric(label="**Remuneração semanal**", value=f"${players_stats['Wage']}")
col3.metric(label="**Clausula de rescisão**", value=f"${players_stats['Release Clause']}")

# st.dataframe(df_data)