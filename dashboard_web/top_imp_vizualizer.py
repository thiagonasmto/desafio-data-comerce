import plotly.express as px
import pandas as pd

def grafico_top_3_importados_estado(df, save_as_html=False):
    # 2. Top 3 produtos mais importados por estado
    importados_estado = df[df['VL_FOB'] < 0].groupby(['SG_UF_NCM', 'CO_NCM'])['QT_ESTAT'].sum().reset_index()
    importados_top_3_estado = importados_estado.sort_values('QT_ESTAT', ascending=False).groupby(['SG_UF_NCM']).head(3)

    # Criar coluna de nome do produto (usando o código mesmo)
    importados_top_3_estado['Produto'] = importados_top_3_estado['CO_NCM'].astype(str)

    # Gerar cores únicas por produto
    produtos = importados_top_3_estado['Produto'].unique()
    cores = px.colors.qualitative.Set2
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(importados_top_3_estado, x='SG_UF_NCM', y='QT_ESTAT',
                 color='Produto',
                 title='Top 3 Produtos Importados por Estado',
                 labels={'SG_UF_NCM': 'Estado', 'QT_ESTAT': 'Quantidade do produto conforme a unidade estatística correspondente'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Importados", itemsizing='constant')
    )

    if save_as_html:
        fig.write_html("grafico_top_3_importados_estado.html")
    else:
        fig.show()
