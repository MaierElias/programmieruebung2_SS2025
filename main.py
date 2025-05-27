import streamlit as st

from PIL import Image

from src.read_data import get_person_names, get_person_data_by_name, get_person_image_by_name


if "selected_person" not in st.session_state:
    st.session_state.selected_person = "Name 1"

st.write("# Hello, Streamlit!")

st.write("## Zweite Überschrift")

st.write ("This is a simple Streamlit app to demonstrate the setup")

st.session_state.selected_person = st.selectbox("Wähle eine Versuchsperson", options = get_person_names())

st.write(st.session_state.selected_person)

# Laden eines Bilds
image = Image.open(get_person_image_by_name(st.session_state.selected_person))
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.selected_person)