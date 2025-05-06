import plotly.express as px
import pandas as pd

def grafico_top_3_exportados_estado(df, save_as_html=False):
    # 1. Top 3 produtos mais exportados por estado
    exportados_estado = df.groupby(['SG_UF_NCM', 'CO_NCM'])['QT_ESTAT'].sum().reset_index()
    exportados_top_3_estado = exportados_estado.sort_values('QT_ESTAT', ascending=False).groupby(['SG_UF_NCM']).head(3)

    # Criar coluna de nome do produto (usando o código mesmo)
    exportados_top_3_estado['Produto'] = exportados_top_3_estado['CO_NCM'].astype(str)

    # Gerar cores únicas por produto
    produtos = exportados_top_3_estado['Produto'].unique()
    cores = px.colors.qualitative.Set1
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(exportados_top_3_estado, x='SG_UF_NCM', y='QT_ESTAT',
                 color='Produto',
                 title='Top 3 Produtos Exportados por Estado',
                 labels={'SG_UF_NCM': 'Estado', 'QT_ESTAT': 'Quantidade do produto conforme a unidade estatística correspondente'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Exportados", itemsizing='constant')
    )

    if save_as_html:
        fig.write_html("grafico_top_3_exportados_estado.html")
    else:
        fig.show()
