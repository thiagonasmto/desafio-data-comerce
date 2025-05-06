import plotly.express as px
import pandas as pd

def grafico_top_3_exportados_mes_estado(df, estado, save_as_html=False):
    # Filtra os dados para o estado especificado
    df_estado = df[df['SG_UF_NCM'] == estado]

    # 3. Top 3 produtos exportados por estado em cada mês
    exportados_mes_estado = df_estado.groupby(['SG_UF_NCM', 'CO_MES', 'CO_NCM'])['QT_ESTAT'].sum().reset_index()
    exportados_top_3_mes_estado = exportados_mes_estado.sort_values('QT_ESTAT', ascending=False).groupby(['SG_UF_NCM', 'CO_MES']).head(3)

    # Criando uma coluna com o nome do produto (aqui assumindo que CO_NCM é o código do produto)
    # Se você tiver um dicionário com o mapeamento de CO_NCM para nome, você pode usá-lo aqui.
    exportados_top_3_mes_estado['Produto'] = exportados_top_3_mes_estado['CO_NCM'].astype(str)

    # Gerando um dicionário para mapear cada produto a uma cor única
    produtos = exportados_top_3_mes_estado['Produto'].unique()
    cores = px.colors.qualitative.Set1  # Usando uma paleta de cores qualitativas
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Cria o gráfico com cores únicas para cada produto, sem texto sobre as barras
    fig = px.bar(exportados_top_3_mes_estado, x='CO_MES', y='QT_ESTAT',
                 title=f'Top 3 Produtos Exportados para o Estado {estado} em Cada Mês',
                 labels={'CO_MES': 'Mês', 'CO_NCM': 'Código NCM', 'QT_ESTAT': 'Quantidade do produto conforme a unidade estatística correspondente'},
                 hover_data={'CO_NCM': True, 'QT_ESTAT': True, 'CO_MES': True},
                 color='Produto',  # A cor será baseada no nome do produto
                 color_discrete_map=color_map)  # Atribuindo cores únicas

    # Removendo o texto das barras
    fig.update_traces(textposition='none')

    # Ajuste na legenda
    fig.update_layout(
        legend_title='Produto',
        legend=dict(
            title="Produtos Exportados",
            itemsizing='constant',
            tracegroupgap=10
        )
    )

    if save_as_html:
        # Salvar o gráfico como um arquivo HTML
        fig.write_html(f"grafico_top_3_exportados_mes_{estado}.html")
    else:
        # Exibir o gráfico no navegador
        fig.show()
