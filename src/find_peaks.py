
#
import pandas as pd
import plotly.express as px
import numpy as np

def find_peaks(df, threshold=340):
    """
    a function that finds R-peaks in an EKG signal.
    """
    list_of_peaks = []	

    for index, row in df.iterrows():   
        if index == df.index.max():
            break 

        current_value = row['Voltage [mV]']

        # ist der current_value größer als der Vorgänger und Nachfolger
        if current_value > df.iloc[index-1]["Voltage [mV]"] and current_value >= df.iloc[index+1]["Voltage [mV]"]:
            print("Found a peak at index: ", index)
            if current_value > threshold:
                list_of_peaks.append(index)
    return list_of_peaks

if __name__ == "__main__":

    df = pd.read_csv('data/ekg_data/01_Ruhe.txt', sep = "	")
    df.columns = ['Voltage [mV]', 'Time [ms]']
    df

    list_of_peaks = find_peaks(df, 350)

    df["is_peak"] = False
    df.loc[list_of_peaks, "is_peak"] = True
    df["is_peak"].value_counts()

    fig = px.line(df, x='Time [ms]', y='Voltage [mV]', title='EKG Data with Peaks Highlighted')
    fig.add_scatter(x=df.loc[df["is_peak"], 'Time [ms]'], 
                    y=df.loc[df["is_peak"], 'Voltage [mV]'], 
                    mode='markers', 
                    marker=dict(color='red', size=5), 
                    name='Peaks')
    fig.show(renderer='browser')

