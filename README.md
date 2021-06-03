# Projeto Desafio Técnico
### Autor: Cesar Costa

 ---

## Conteúdo

- [Sobre](#about)
- [Primeiros Passos](#getting_started)
- [Uso](#usage)
- [Contribuidores](#contributing)

 ---

## Sobre <a name = "about"></a>

#### Desafio técnico para examinar as noções das implementações da linguagem Python com o framework Django.

## Primeiros Passos <a name = "getting_started"></a>

### Pré-requisitos

#### Instalação dos pré-requisitos do projeto para executar em sua máquina deve ser feita com Python 3 e o ambiente virtualenv.
#### Porém, esse projeto pode ser feito utilizando Docker. Ao final desse README têm links para rodar o projeto utilizando docker no WLS.

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
pip install -r requirements-dev.txt
```

## Uso <a name = "usage"></a>
#### Comandos para executar o servidor em sua máquina:

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

## Fontes

### Tutorial docker desenvolvimento:
#### http://marcusalmeida.github.io/2016/desenvolvendo-com-django-docker-compose/

### Correção de instalação de docker no WSL Ubuntu-18.04:
#### https://stackoverflow.com/questions/48047810/cannot-connect-to-the-docker-daemon-on-bash-on-ubuntu-windows