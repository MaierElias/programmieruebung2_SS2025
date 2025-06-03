import streamlit as st
import pandas as pd

from PIL import Image

from src.read_data import get_person_names, get_person_data_by_name, get_person_image_by_name

from src.analyze_activity_data import create_plot, dataframe

if "selected_person" not in st.session_state:
    st.session_state.selected_person = "Name 1"

st.write("# Hello, Streamlit!")

st.write("## Zweite Überschrift")

st.write ("This is a simple Streamlit app to demonstrate the setup")

st.session_state.selected_person = st.selectbox("Wähle eine Versuchsperson", options = get_person_names())

st.write(st.session_state.selected_person)

# Laden eines Bilds
selected_person_data = get_person_data_by_name(st.session_state.selected_person)
image = Image.open(get_person_image_by_name(st.session_state.selected_person))
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.selected_person)

# Input der maximalen Herzfrequenz
max_hr = st.number_input(
    "Bitte maximale Herzfrequenz eingeben:",
    min_value=100,
    max_value=250,
    value=190,
    step=1
)
# Darstellen der Daten

st.plotly_chart(create_plot(max_hr))

# Hinzufügen der Tabelle (Durchschnittsleistung pro Zone und verbrachte Zeit in Minuten pro Zone)

zone_counts = dataframe["Zone"].value_counts().rename("Verbrachte Zeit / [min]").sort_index(ascending = False)/60 # Zonen-Häufigkeit (Minuten pro Zone)

mean_power_per_zone = dataframe.groupby("Zone")["PowerOriginal"].mean().rename("Durchschnittsleistung / [W]").sort_index() # Durchschnittsleistung pro Zone

result_df = pd.concat([zone_counts, mean_power_per_zone], axis=1) # Zusammenführen der Daten

st.dataframe(result_df)

