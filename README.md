# Teams Dashboard

## Descrição do Projeto

O projeto "Teams Dashboard" é uma aplicação web interativa desenvolvida com Streamlit que permite visualizar informações sobre clubes de futebol e seus jogadores. A interface é amigável e permite que os usuários selecionem um clube específico para visualizar detalhes dos jogadores, como idade, valor de mercado, salário, entre outros.

## Funcionalidades

- **Seleção de Clube**: O usuário pode selecionar um clube de uma lista suspensa para visualizar os jogadores associados a esse clube.
- **Exibição de Informações**: Para cada jogador, são exibidas informações como:
  - Idade
  - Foto
  - Bandeira do país
  - Avaliação geral
  - Valor de mercado
  - Salário
  - Data de ingresso no clube
  - Altura
  - Peso
  - Validade do contrato
- **Visualização de Dados**: A aplicação utiliza tabelas interativas para exibir os dados dos jogadores, com colunas que incluem gráficos de progresso para avaliação e salário.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas em Python.
- **Pandas**: Biblioteca para manipulação e análise de dados.

## Instalação

Para executar este projeto, você precisará ter o Python e as bibliotecas necessárias instaladas. Siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/ricardochomicz/streamlit_fifa.git
   cd seu_repositorio
   ```

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

2. Instale as dependências:
```bash
pip install streamlit pandas
```

3. Execute o aplicativo:
```bash
python -m streamlit run 1_home.py
```