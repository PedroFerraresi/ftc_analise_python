import pandas as pd

from .process_data import process_data

# 1. Quantos restaurantes únicos estão registrados?
# 2. Quantos paises únicos estão registrados?
# 3. Quantas cidades únicas estão registradas?
# 4. Qual o total de avaliações feitas?
# 5. Qual o total de tipos de culinária registrados?


def qty_restaurants(dataframe):
    return dataframe.shape[0]


def qty_countries(dataframe):
    return dataframe.loc[:, "country"].nunique()


def qty_cities(dataframe):
    return dataframe.loc[:, "city"].nunique()


def qty_ratings(dataframe):
    return dataframe.loc[:, "votes"].sum()


def qty_cuisines(dataframe):
    return dataframe.loc[:, "cuisines"].nunique()
