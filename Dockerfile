# Tutorial docker desenvolvimento: http://marcusalmeida.github.io/2016/desenvolvendo-com-django-docker-compose/
FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /code

# Define o diretório de trabalho
WORKDIR /code

# "Copia" arquivo requirements.txt para o diretorio code
ADD requirements.txt /code/

# Executa o pip
RUN pip install -r requirements.txt

# "Copia" os arquivos locais para o diretorio code no container 
ADD . /code/