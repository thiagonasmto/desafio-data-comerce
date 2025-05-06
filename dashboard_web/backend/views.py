from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
import os
from ..get_data_bd import gerar_graficos

def home_view(request):
    return JsonResponse({"message": "API de upload de CSV funcionando."})

class UploadCSVView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)

        table_name = os.path.splitext(file.name)[0]

        # Configurações do banco
        db = settings.DATABASES['default']
        engine = create_engine(f"postgresql://{db['USER']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['NAME']}")

        try:
            df = pd.read_csv(file, sep=';', encoding='utf-8')
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            return Response({"message": f"Tabela '{table_name}' carregada com sucesso."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def gerar_top_3_exportados(request):
    try:
        gerar_graficos()
        return JsonResponse({"message": "Gráfico gerado com sucesso!"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)