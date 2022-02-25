# projeto-web-django

Construção de uma aplicação web real utilizando django

Acesse em -> https://projetowebdjango.herokuapp.com/

[![Updates](https://pyup.io/repos/github/henriquelima1984/projeto-web-django/shield.svg)](https://pyup.io/repos/github/henriquelima1984/projeto-web-django/)
[![Python 3](https://pyup.io/repos/github/henriquelima1984/projeto-web-django/python-3-shield.svg)](https://pyup.io/repos/github/henriquelima1984/projeto-web-django/)
[![codecov](https://codecov.io/gh/henriquelima1984/projeto-web-django/branch/main/graph/badge.svg?token=9UOHWJMH4C)](https://codecov.io/gh/henriquelima1984/projeto-web-django)
[![Django CI](https://github.com/henriquelima1984/projeto-web-django/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/henriquelima1984/projeto-web-django/actions/workflows/python-app.yml)

Passo a passo:

1 - Instale o pipenv e depois todas as dependências do projeto.

```console
pip install -q pipenv
pipenv sync --dev
```

2 - Para rodar flake8, pytest and codecov
```console
pipenv run flake8
pipenv run pytest --cov=nome do pacote
pipenv run codecov
```