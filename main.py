import streamlit as st
import pandas as pd

from PIL import Image

from src.read_data import get_person_names, get_person_data_by_name, get_person_image_by_name
from src.person import Person
from src.ekgdata import EKGdata
from src.analyze_activity_data import create_plot, dataframe

if "selected_person" not in st.session_state:
    st.session_state.selected_person = "Name 1"

st.write("# Hello, Streamlit!")

st.write("## Zweite Überschrift")

st.write ("This is a simple Streamlit app to demonstrate the setup")

person_data = Person.load_person_data()
list_of_persons = Person.get_person_list(person_data)

st.session_state.selected_person = st.selectbox("Wähle eine Versuchsperson", options = list_of_persons)

st.write(st.session_state.selected_person)

# Laden eines Bilds
selected_person_data = Person.find_person_data_by_name(str(st.session_state.selected_person))
person_image = selected_person_data["picture_path"]
image = Image.open(person_image)
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

# Hinzufügen der EKG-Daten
threshold = st.number_input(
    "Bitte Schwellenwert für EKG-Peaks eingeben:",
    min_value=100,
    max_value=500,
    value=340,
    step=1
)
# Darstellen der Daten
ekg_dict = selected_person_data["ekg_tests"][0] 
ekg_data = EKGdata(ekg_dict)
st.plotly_chart(ekg_data.plot_time_series(threshold))
# Anzeigen der geschätzten durchschnittlichen Herzfrequenz
heart_rate = ekg_data.estimate_heart_rate(threshold)
if heart_rate is not None:
    st.write(f"Geschätzte Herzfrequenz: {heart_rate} [BPM]")