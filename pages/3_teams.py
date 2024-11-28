import streamlit as st

st.set_page_config(
    layout="wide",  # Define o layout da página como "wide" (amplo).
    page_icon="🏳️",  # Define o ícone da página.
    page_title="Teams",  # Define o título da página.
)

df_data = st.session_state["data"]

clubs = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubs)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value", "Wage", "Joined", 
           "Height", "Weight", "Contract Valid Until"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall",
                     format="%d",
                     min_value=0,
                     max_value=100,
                     width="small"
                 ),
                 "Wage": st.column_config.ProgressColumn(
                     "Weekly Wage", 
                     format="£%f",
                     min_value=0,
                     max_value=df_filtered["Wage"].max(),
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
             })
