import streamlit as st
import pandas as pd
import plotly.express as px

# Função para criar o gráfico top 3 exportados por todos os estados
def grafico_top_3_exportados_estado(df, ano_selecionado):
    # 1. Top 3 produtos mais exportados por todos os estados
    df_exp = df[(df["tipo"] == "Exportação") & (df["ano"] == ano_selecionado)]  # Filtro de ano adicionado
    exportados_estado = df_exp.groupby(['estado', 'produto'])['quantidade'].sum().reset_index()
    exportados_top_3_estado = exportados_estado.sort_values('quantidade', ascending=False).groupby(['estado']).head(3)

    # Gerar cores únicas por produto
    produtos = exportados_top_3_estado['produto'].unique()
    cores = px.colors.qualitative.Set1
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(exportados_top_3_estado, x='estado', y='quantidade',
                 color='produto',
                 title=f'Top 3 Produtos Exportados por Todos os Estados - {ano_selecionado}',
                 labels={'estado': 'Estado', 'quantidade': 'Quantidade das Exportações'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Exportados", itemsizing='constant')
    )

    return fig

# Função para criar o gráfico top 3 exportados por estado selecionado
def grafico_top_3_exportados_estado_selecionado(df, estado_selecionado, ano_selecionado):
    # Filtra os dados para o ano e estado selecionado
    df_exp_estado = df[(df["tipo"] == "Exportação") &
                       (df["estado"] == estado_selecionado) &
                       (df["ano"] == ano_selecionado)]

    # 1. Top 3 produtos mais exportados por estado selecionado
    exportados_estado = df_exp_estado.groupby(['estado', 'produto'])['quantidade'].sum().reset_index()
    exportados_top_3_estado = exportados_estado.sort_values('quantidade', ascending=False).head(3)

    # Gerar cores únicas por produto
    produtos = exportados_top_3_estado['produto'].unique()
    cores = px.colors.qualitative.Set1
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(exportados_top_3_estado, x='estado', y='quantidade',
                 color='produto',
                 title=f'Top 3 Produtos Exportados por Estado: {estado_selecionado} - {ano_selecionado}',
                 labels={'estado': 'Estado', 'quantidade': 'Quantidade das Exportações'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Exportados", itemsizing='constant')
    )

    return fig

# Função para o gráfico mensal de exportação em 2021
def grafico_mensal_exportacao(df, estado_selecionado):
    df_exp_2021 = df[(df["tipo"] == "Exportação") &
                     (df["estado"] == estado_selecionado) &
                     (df["ano"] == 2021)]
    
    grupo_mes = df_exp_2021.groupby(["mes", "produto"])["quantidade"].sum().reset_index()
    top_mes = grupo_mes.sort_values(["mes", "quantidade"], ascending=[True, False])
    top3_mes = top_mes.groupby("mes").head(3)

    fig_mes = px.bar(
        top3_mes,
        x="mes",
        y="quantidade",
        color="produto",
        title=f"Top 3 Produtos Exportados por Mês – 2021 ({estado_selecionado})",
        labels={'mes': 'Mês', 'quantidade': 'Quantidade Exportada'}
    )
    
    return fig_mes

# Função para criar o gráfico top 3 importados por todos os estados
def grafico_top_3_importados_estado(df, ano_selecionado):
    # 1. Top 3 produtos mais importados por todos os estados
    df_imp = df[(df["tipo"] == "Importação") & (df["ano"] == ano_selecionado)]  # Filtro de ano adicionado
    importados_estado = df_imp.groupby(['estado', 'produto'])['quantidade'].sum().reset_index()
    importados_top_3_estado = importados_estado.sort_values('quantidade', ascending=False).groupby(['estado']).head(3)

    # Gerar cores únicas por produto
    produtos = importados_top_3_estado['produto'].unique()
    cores = px.colors.qualitative.Set1
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(importados_top_3_estado, x='estado', y='quantidade',
                 color='produto',
                 title=f'Top 3 Produtos Importados por Todos os Estados - {ano_selecionado}',
                 labels={'estado': 'Estado', 'quantidade': 'Quantidade das Importações'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Importados", itemsizing='constant')
    )

    return fig

# Função para criar o gráfico top 3 importados por estado selecionado
def grafico_top_3_importados_estado_selecionado(df, estado_selecionado, ano_selecionado):
    # Filtra os dados para o ano e estado selecionado
    df_imp_estado = df[(df["tipo"] == "Importação") &
                       (df["estado"] == estado_selecionado) &
                       (df["ano"] == ano_selecionado)]

    # 1. Top 3 produtos mais importados por estado selecionado
    importados_estado = df_imp_estado.groupby(['estado', 'produto'])['quantidade'].sum().reset_index()
    importados_top_3_estado = importados_estado.sort_values('quantidade', ascending=False).head(3)

    # Gerar cores únicas por produto
    produtos = importados_top_3_estado['produto'].unique()
    cores = px.colors.qualitative.Set1
    color_map = {produto: cores[i % len(cores)] for i, produto in enumerate(produtos)}

    # Gráfico com legenda por produto
    fig = px.bar(importados_top_3_estado, x='estado', y='quantidade',
                 color='produto',
                 title=f'Top 3 Produtos Importados por Estado: {estado_selecionado} - {ano_selecionado}',
                 labels={'estado': 'Estado', 'quantidade': 'Quantidade das Importações'},
                 color_discrete_map=color_map)

    fig.update_traces(textposition='none')

    fig.update_layout(
        legend_title='Produto',
        legend=dict(title="Produtos Importados", itemsizing='constant')
    )

    return fig

# Função para o gráfico mensal de importação em 2021
def grafico_mensal_importacao(df, estado_selecionado):
    df_imp_2021 = df[(df["tipo"] == "Importação") &
                     (df["estado"] == estado_selecionado) &
                     (df["ano"] == 2021)]
    
    grupo_mes = df_imp_2021.groupby(["mes", "produto"])["quantidade"].sum().reset_index()
    top_mes = grupo_mes.sort_values(["mes", "quantidade"], ascending=[True, False])
    top3_mes = top_mes.groupby("mes").head(3)

    fig_mes = px.bar(
        top3_mes,
        x="mes",
        y="quantidade",
        color="produto",
        title=f"Top 3 Produtos Importados por Mês – 2021 ({estado_selecionado})",
        labels={'mes': 'Mês', 'quantidade': 'Quantidade Importada'}
    )
    
    return fig_mes

# Streamlit Setup
st.set_page_config(page_title="Dashboard Comércio Exterior", layout="wide")

st.title("📦 Dashboard – Top 3 Produtos por NCM")

st.sidebar.header("📁 Carregamento de Arquivos")

# Carregar múltiplos arquivos
uploaded_files = st.sidebar.file_uploader("Carregue os arquivos de Exportação e Importação", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    # Inicializa os dataframes
    df_exp = pd.DataFrame()
    df_imp = pd.DataFrame()

    # Processa os arquivos carregados
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name

        # Leitura do arquivo com separador ;
        df = pd.read_csv(uploaded_file, sep=";")
        
        # Renomeia colunas padronizadas
        rename_cols = {
            "CO_ANO": "ano",
            "CO_MES": "mes",
            "CO_NCM": "produto",
            "SG_UF_NCM": "estado",
            "VL_FOB": "valor",
            "QT_ESTAT": "quantidade"
        }
        df.rename(columns=rename_cols, inplace=True)

        # Identifica se é exportação ou importação com base no prefixo do nome do arquivo
        if file_name.startswith("IMP"):
            df["tipo"] = "Importação"
            df_imp = pd.concat([df_imp, df], ignore_index=True)
        elif file_name.startswith("EXP"):
            df["tipo"] = "Exportação"
            df_exp = pd.concat([df_exp, df], ignore_index=True)

    # Junta os dois dataframes
    df = pd.concat([df_exp, df_imp], ignore_index=True)

    # Conversões de tipos
    df['ano'] = df['ano'].astype(int)
    df['mes'] = df['mes'].astype(int)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df = df.dropna(subset=['valor'])

    # Filtros
    estados = sorted(df["estado"].dropna().unique())
    estado_selecionado = st.sidebar.selectbox("Selecione o Estado para o gráfico mensal", estados)

    anos_disponiveis = sorted(df["ano"].unique(), reverse=True)
    ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos_disponiveis)

    st.markdown(f"### Ano: **{ano_selecionado}**")

    # Exibe os gráficos
    fig_top_3_exportados_estado = grafico_top_3_exportados_estado(df, ano_selecionado)
    st.plotly_chart(fig_top_3_exportados_estado, use_container_width=True)

    fig_top_3_importados_estado = grafico_top_3_importados_estado(df, ano_selecionado)
    st.plotly_chart(fig_top_3_importados_estado, use_container_width=True)

    fig_top_3_exportados_estado_selecionado = grafico_top_3_exportados_estado_selecionado(df, estado_selecionado, ano_selecionado)
    st.plotly_chart(fig_top_3_exportados_estado_selecionado, use_container_width=True)

    fig_top_3_importados_estado_selecionado = grafico_top_3_importados_estado_selecionado(df, estado_selecionado, ano_selecionado)
    st.plotly_chart(fig_top_3_importados_estado_selecionado, use_container_width=True)

    fig_mensal_exportacao = grafico_mensal_exportacao(df, estado_selecionado)
    st.plotly_chart(fig_mensal_exportacao, use_container_width=True)

    fig_mensal_importacao = grafico_mensal_importacao(df, estado_selecionado)
    st.plotly_chart(fig_mensal_importacao, use_container_width=True)

else:
    st.info("👈 Carregue os arquivos de **exportação e importação** para visualizar os gráficos.")