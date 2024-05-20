# Sea Level Predictor

Este projeto prevê o aumento do nível do mar até o ano de 2050, usando dados históricos fornecidos pela [EPA (Environmental Protection Agency)](https://www.epa.gov/).

## Visão Geral

O objetivo deste projeto é analisar os dados históricos do nível do mar e prever o aumento futuro usando regressão linear. O projeto cria um gráfico de dispersão dos dados históricos, adiciona linhas de melhor ajuste (uma para todos os dados e outra para os dados recentes desde 2000), e anota as previsões para o ano de 2050.

## Estrutura do Projeto

- **import_data**: Importa os dados do nível do mar a partir de um arquivo CSV.
- **create_scatter_plot**: Cria um gráfico de dispersão dos dados importados.
- **plot_line_of_best_fit**: Plota uma linha de melhor ajuste com base nos dados fornecidos.
- **predict_sea_level**: Prediz o nível do mar para um ano específico usando a equação da linha de melhor ajuste.
- **add_annotations**: Adiciona anotações ao gráfico para destacar previsões específicas.
- **add_labels_and_title**: Adiciona rótulos e título ao gráfico.
- **show_plot**: Exibe o gráfico gerado.

## Instalação

1. Clone o repositório para o seu diretório local:

   ```bash
   git clone https://github.com/seu-usuario/sea-level-predictor.git
   cd sea-level-predictor

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv env
   source env/bin/activate   # Para Linux/macOS
   env\Scripts\activate      # Para Windows

3. Instale as dependências necessárias:
    ```bash
     pip install -r requirements.txt
