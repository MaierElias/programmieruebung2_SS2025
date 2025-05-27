import streamlit as st

if "selected_person" not in st.session_state:
    st.session_state.selected_person = "Name 1"

st.write("# Hello, Streamlit!")

st.write("## Zweite Überschrift")

st.write ("This is a simple Streamlit app to demonstrate the setup")

st.session_state.selected_person = st.selectbox("Wähle eine Versuchsperson", options=["Name 1", "Name 2", "Name 3"])

st.write(st.session_state.selected_person)
