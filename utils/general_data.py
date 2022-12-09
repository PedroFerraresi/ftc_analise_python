import pandas as pd

from .process_data import process_data


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
