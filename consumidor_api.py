# NESSE ARQUIVO SE CONCENTRARÁ A LÓGICA DE COMUNICAÇÃO DA API E DE
# INTERPRETAÇÃO DA RESPOSTA.



import requests # BIBLIOTECA REQUESTS SIMPLIFICA AS REQUISIÇÕES HTTP EM PYTHON
import os
from dotenv import load_dotenv # BIBLIOTECA DOTENV PARA PEGAR CREDENCIAIS PRIVADAS NO .ENV

url = os.getenv("database")

parametros = { # PARÂMETROS SÃO INFORMAÇÕES ENVIADAS PARA DEFINIR O CONTEÚDO SOLICITADO
    "longitude": -48.8456,
    "latitude": -26.3044,
    "current": "temperature_2m, relative_humidity_2m, apparent_temperature, time"}


resposta = requests.get(
    url,
    params=parametros,
    timeout=15
)

resposta.raise_for_status()dados = resposta.json()







