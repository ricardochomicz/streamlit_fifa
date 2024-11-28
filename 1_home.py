import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/FIFA23_official_data.csv", index_col=0)
    
    df_data["Contract Valid Until"] = pd.to_datetime(df_data["Contract Valid Until"], errors='coerce')
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.now()]
    # df_data = df_data[df_data["Value"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.markdown("# FIFA 2023 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Ricardo Chomicz](https://www.github.com/ricardochomicz/)")

st.markdown(
    """
    Comparação histórica entre Messi e Ronaldo (quais atributos de habilidade mais mudaram ao longo do tempo – em comparação com as estatísticas da vida real);
Orçamento ideal para criar uma equipe competitiva (no nível das n melhores equipes da Europa) e nesse ponto o orçamento não permite comprar jogadores significativamente melhores para a escalação de 11 homens. Um extra é a mesma comparação com o atributo Potencial para a escalação em vez do atributo Geral;
Análise de amostra dos melhores n% de jogadores (por exemplo, top 5% do jogador) para ver se alguns atributos importantes como Agilidade ou Controle de Bola ou Força foram populares ou não nas versões do FIFA. Um exemplo seria ver que os 5% melhores jogadores do FIFA 20 são mais rápidos (maior Aceleração e Agilidade) em comparação com o FIFA 15. A tendência dos atributos também é uma indicação importante de como alguns atributos são necessários para que os jogadores ganhem jogos (uma versão com mais jogadores top 5% com estatísticas altas de BallControl indicaria que o jogo é mais focado na técnica do que no aspecto físico).
Conteúdo

Todos os jogadores disponíveis no FIFA 15, 16, 17, 18, 19, 20, 21, 22 e também no FIFA 23
100+ atributos
URL dos jogadores raspados
URL dos rostos dos jogadores carregados, logotipos de clubes e nações
Posições dos jogadores, com o papel no clube e na seleção nacional
Atributos do jogador com estatísticas como Ataque, Habilidades, Defesa, Mentalidade, Habilidades de GR, etc.
Dados pessoais do jogador como nacionalidade, clube, data de nascimento, salário, salário, etc.
As atualizações do conjunto de dados anterior do FIFA 21 são as seguintes:

Inclusão de dados do FIFA 23
Inclusão de todas as jogadoras
Reordenação de colunas – para aumentar a legibilidade
Remoção de campos de atributo GK duplicados
A marcação de defesa de campo foi renomeada para defesa de reconhecimento de marcação e inclui os valores de marcação (nome do atributo antigo – até FIFA 19) e de consciência defensiva (novo nome do atributo – do FIFA 20)
Fonte e Licença: https://sports-statistics.com/sports-data/
""")

btn = st.link_button(
    "Acesse os dados no Kaggle",
    "https://www.kaggle.com/datasets/joebeachcapital/fifa-players"
)
