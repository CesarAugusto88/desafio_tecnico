# Projeto Desafio Técnico
### Autor: Cesar Costa

![alt-text](https://github.com/CesarAugusto88/desafio_tecnico/blob/main/print%20gif/Webp.net-gifmaker.gif)

 ---

## Conteúdo

- [Sobre](#about)
- [Primeiros Passos](#getting_started)
- [Uso](#usage)
- [Contribuidores](#contributing)
- [Instalações WSL](#instalacoes)
- [Resoluções do desafio](#resolucoes)
- [Créditos](#creditos)

 ---

## Sobre <a name = "about"></a>

#### Desafio técnico para examinar as noções das implementações da linguagem Python com o framework Django.

## Primeiros Passos <a name = "getting_started"></a>

### Pré-requisitos

#### Instalação dos pré-requisitos do projeto para executar em sua máquina deve ser feita com Python 3 e o ambiente virtualenv.
#### Porém, esse projeto foi feito utilizando Docker. Ao final desse README têm links para rodar o projeto utilizando docker.

#### Clonar o repositório e entrar no diretório:

```
git clone https://github.com/CesarAugusto88/desafio_tecnico.git
cd desafio_tecnico
```

#### Instalação da virtualenv:

```
python -m venv venv
```

#### Ativar o ambiente virtual .env no prompt do Windowns:

```
venv\Scripts\activate
```

#### Ativar o ambiente virtual .env no Linux e MAC:

```
. venv/bin/activate
```

### Instalação

#### Comando para instalar os requisitos do projeto:

```
pip install -r requirements.txt
```

## Uso <a name = "usage"></a>
#### Comandos para executar as migrações e o servidor em sua máquina:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Comando para criar um super usuário:

```
python manage.py createsuperuser
```

### Lideres do Projeto <a name = "contributing">

 - [Cesar Costa](https://github.com/cesaraugusto88)
 - Leonardo
 - Carlos

 ---

![GitHub](https://img.shields.io/github/license/CesarAugusto88/desafio_tecnico)

##

![GitHub followers](https://img.shields.io/github/followers/CesarAugusto88?%20Follow&style=social)

##


![GitHub.io](https://img.shields.io/badge/Github.io-CesarAugusto88.github.io-red)

 ---

## Instalações <a name = "instalacoes"></a>

### Instalação de pacotes do python 3:
```
sudo apt install -y python3-pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```

### Instalação de docker docker-compose no WSL Ubuntu-20.04:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo pip3 install docker-compose
sudo "PATH=$PATH" docker-compose
sudo "PATH=$PATH:/home/cesar/.local/bin" docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
which docker-compose
```

### Ao "buildar" com o comando a seguir ocorre um erro.
```
sudo /home/cesar/usr/local/bin/docker-compose up
sudo docker-compose up
```

### Erro:
```
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
```

### Correção:
```
sudo dockerd
```

### Stop docker:
```
sudo service docker stop
```

### Start docker:
```
sudo service docker start
```

### Executar comando hello world:
```
docker run hello-world
```

### Mensagem exibida:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete
Digest: sha256:5122f6204b6a3596e048758cabba3c46b1c937a46b5be6225b835d091b90e46c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Para construir o docker-compose com novos requirements:
```
sudo service docker status
sudo service docker stop
sudo service docker start
docker-compose build
docker-compose up
```

### Derrubar e subir docker:
```
docker-compose down
docker-compose up
```

### Executar docker docker-compose e fazer migração no servidor:
```
sudo service docker start
docker-compose build
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```
 ---

## Resoluções do desafio <a name = "resolucoes">:

### 1 - Crie autenticação de usuários e atribua os links aos usuários. :heavy_check_mark: :question:

#### Faltando redirecione para o link real.

### 2 - Crie um contador de acesso link e exiba para o usuários quando logado. :x: :question:

### 3 - Ambientes de dev, homologação e produção. :white_check_mark:
#### Os ambientes foram separado utilizando o pacote Python Decouple.
#### Arquivo .env:
```
SECRET_KEY=###%%%***Sua_Chave***%%%###
DEBUG=True
```
 ---
## DEBUG para produção deve ser False
 ---

### Configuração do settings.py:
```
SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)
```
 ---
#### Obs.: Com esse pacote pode-se fazer configurações de senhas de banco de dados e IP de servidores.
 ---
### 4 - Crie o ambiente de dev baseado em docker. :heavy_check_mark:
#### Ambiente de desenvolvimento foi utilizado doker.

### 5 - Crie um botão de relatório que o usuário consiga  imprimir o numero de acessos separado por dia da semana. :x:
#### Feito somente contagem de número de atualizações de perfil.

### 6 - Crie uma estrutura de deploy baseado em containers. :x: :question:

 ---

## Créditos <a name = "creditos">

### Tutorial desenvolvendo com django docker compose:
 - [Marcus Almeida](http://marcusalmeida.github.io/2016/desenvolvendo-com-django-docker-compose/)

### Projeto dShortener - Um encurtador de URLs feito em Django:
 - [Douglas Miranda](https://github.com/douglasmiranda/dshortener)

### Projeto E-commerce:
 - [Luiz Otávio](https://github.com/luizomf/django-simple-ecommerce)