import streamlit as st

import utils.countries_data as cdt


def make_sidebar(df):
    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return list(countries)


def main():
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    df = cdt.read_processed_data()

    countries = make_sidebar(df)

    st.markdown("# :earth_americas: Visão Países")

    fig = cdt.countries_restaurants(countries)

    st.plotly_chart(fig, use_container_width=True)

    fig = cdt.countries_cities(countries)

    st.plotly_chart(fig, use_container_width=True)

    votes, plate_price = st.columns(2)

    with votes:
        fig = cdt.countries_mean_votes(countries)

        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = cdt.countries_average_plate(countries)

        st.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == "__main__":
    main()
