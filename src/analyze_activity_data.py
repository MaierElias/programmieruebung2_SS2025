
#%% Zelle 1
import pandas as pd

dataframe = pd.read_csv('data/activities/activity.csv')
dataframe
# %%
dataframe["PowerOriginal"].mean()
dataframe["PowerOriginal"].max()

# %%
dataframe["PowerOriginal"].plot()
# %% Wie lange mehr als 300 Watt?

dataframe["PowerOriginal"] > 300

dataframe["HighPower"] = dataframe["PowerOriginal"] > 300
dataframe["HighPower"].sum()
dataframe["HighPower"].value_counts()

# %%
dataframe["Zone"] = None

hr_max = dataframe["HeartRate"].max()
hr_max

# %%
untergrenzen_zonen = {}
zone = 1
for faktor in range(50, 100, 10):	
    untergrenzen_zonen[f"Zone {zone}"] = float(hr_max * faktor/100)
    # print("Zone", zone)
    # print(hr_max * faktor)
    zone += 1

untergrenzen_zonen
# %% Füge eine neue Spalte Zone hinzu, die die Zone basierend auf der Herzfrequenz angibt
list_zone = []

dataframe["Zone"] = None

for index, row in dataframe.iterrows():
    #print(row["HeartRate"])
    current_hr = row["HeartRate"]
    if current_hr >= untergrenzen_zonen["Zone 5"]:
        list_zone.append("Zone 5")
    elif current_hr >= untergrenzen_zonen["Zone 4"]:
        list_zone.append("Zone 4")
    elif current_hr >= untergrenzen_zonen["Zone 3"]:
        list_zone.append("Zone 3")
    elif current_hr >= untergrenzen_zonen["Zone 2"]:
        list_zone.append("Zone 2")
    elif current_hr >= untergrenzen_zonen["Zone 1"]:
        list_zone.append("Zone 1")
    else:
        list_zone.append("Zone 0")

dataframe["Zone"] = list_zone

dataframe["Zone"].value_counts()
# %%
df_groups = dataframe.groupby("Zone").mean()
df_groups[["PowerOriginal", "HeartRate"]]
# %% erstellen eines interaktiven Plots
import plotly.express as px
def create_plot():
    fig = px.line(dataframe[["PowerOriginal", "HeartRate"]], y = ["PowerOriginal", "HeartRate"])
    fig.show()
    return fig
# %%
