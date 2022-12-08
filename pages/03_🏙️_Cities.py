# Contents of ~/my_app/pages/page_3.py
import streamlit as st


def make_sidebar():
    st.sidebar.markdown("# Cities 🏙️")


def main():
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

    st.markdown("# Cities 🏙️")


if __name__ == "__main__":
    main()
