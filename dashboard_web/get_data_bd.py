# get_data_bd.py
import os
import django
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine
from top_exp_vizualizer import grafico_top_3_exportados_estado
from top_imp_vizualizer import grafico_top_3_importados_estado
from top_exp_per_month import grafico_top_3_exportados_mes_estado

def gerar_graficos():
    # Configura ambiente Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup()

    # Conecta ao banco
    db_settings = settings.DATABASES['default']
    engine = create_engine(f"postgresql://{db_settings['USER']}:{db_settings['PASSWORD']}@{db_settings['HOST']}:{db_settings['PORT']}/{db_settings['NAME']}")

    # Nome da tabela que você carregou
    TABLE_NAME = 'EXP_2020'

    # Lê a tabela para um DataFrame
    df = pd.read_sql_table(TABLE_NAME, engine)

    # Mostra primeiras linhas
    print(df.head())

    # Chamar códigos para plotar gráficos abaixo
    grafico_top_3_exportados_estado(df, save_as_html=True)
    grafico_top_3_importados_estado(df, save_as_html=True)
    grafico_top_3_exportados_mes_estado(df,'RN', save_as_html=True)