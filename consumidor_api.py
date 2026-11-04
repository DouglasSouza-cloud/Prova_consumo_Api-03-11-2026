# NESSE ARQUIVO SE CONCENTRARÁ A LÓGICA DE COMUNICAÇÃO DA API E DE
# INTERPRETAÇÃO DA RESPOSTA.



import requests # BIBLIOTECA REQUESTS SIMPLIFICA AS REQUISIÇÕES HTTP EM PYTHON
import os
from dotenv import load_dotenv # BIBLIOTECA DOTENV PARA PEGAR CREDENCIAIS PRIVADAS NO .ENV

url = "https://api.open-meteo.com/v1/forecast"

parametros = { # PARÂMETROS SÃO INFORMAÇÕES ENVIADAS PARA DEFINIR O CONTEÚDO SOLICITADO
    "latitude": -26.3044,
    "longitude": -48.8456,
    "current": "temperature_2m"}


resposta = requests.get(
    url,
    params=parametros,
    timeout=15
)
dados = resposta.json()

print (resposta)
print (dados)