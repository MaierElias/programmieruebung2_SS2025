
#%% Zelle 1
import pandas as pd

dataframe = pd.read_csv('../data/activities/activity.csv')
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
