# load_csv.py
import os
import django
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine

# Configura o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Caminho para o arquivo CSV
csv_path = os.path.join('data', 'EXP_2020.csv')

# Extrai as configurações do banco do settings.py
db_settings = settings.DATABASES['default']

DB_USER = db_settings['USER']
DB_PASSWORD = db_settings['PASSWORD']
DB_HOST = db_settings['HOST']
DB_PORT = db_settings['PORT']
DB_NAME = db_settings['NAME']

# Nome da tabela no banco
TABLE_NAME = 'EXP_2020'

# Cria conexão com o banco
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Lê o CSV
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')

# Salva no banco
df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)

print(f'Tabela "{TABLE_NAME}" carregada com sucesso!')
