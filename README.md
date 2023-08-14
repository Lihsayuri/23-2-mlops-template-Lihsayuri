# 23-2-mlops-template-Lihsayuri

### Feito por :sassy_woman:

- Lívia Sayuri Makuta.

### Objetivo :round_pushpin:

Esse repositório foi criado para servir de template para projetos de Machine Learning. Como vimos em aula, em um ambiente de produção que na maioria das vezes precisa ser escalável, é necessário estabelecer padrões de organização. Isso facilita na criação de novos argumentos e análises de novas features em um modelo, por exemplo. É por isso que isso repositório foi criado - com o `cookiecutter`, para ser um template a ser usado em projetos futuros. Ele segue a seguinte estrutura:

- data
- notebooks
- models
- src
```

As quatro vão exercer os seguintes papéis:

- `data`: vai ser a pasta responsável por armazenar todos os dados utilizados no projeto. 
- `notebooks`: essa será a pasta que conterá todos os jupyter notebooks utilizados no projeto. 
- `models`: essa será a pasta que armazenará todos os modelos utilizados, desde OneHotEncoder até modelos com Random Forest, etc.
- `src`: essa será a pasta que de fato armazenará os códigos de pré-processamento, treinamento e predição, os quais correspondem aos seguintes documentos: `__init__.py`, `process.py`, `train.py` e `predict.py`. 