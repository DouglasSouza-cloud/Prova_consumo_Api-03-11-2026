# Clonar o repositório em um diretório de sua preferência (recomendável em "Documentos" da área de trabalho)
git clone url_do_repositório

# PRIMEIRO PASSO IMPORTANTE!: INSTALAR AS DEPENDÊNCIAS DO PROJETO
No terminal rode: pip install -r requirements.txt
Rode também: copy .env.example .env (Serve para copiar as informações do arquivo .env.example para .env, 
já criando ele no processo)

Após isso coloque o endpoint da api no lugar das aspas
# PARA RODAR A APLICAÇÃO, EXECUTE:
python consumidor_api.py