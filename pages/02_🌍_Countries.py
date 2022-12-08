# Contents of ~/my_app/pages/page_3.py
import streamlit as st


def make_sidebar():
    st.sidebar.markdown("# Restaurants :earth_americas:")


def main():
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    st.markdown("# Restaurants :earth_americas:")


if __name__ == "__main__":
    main()
