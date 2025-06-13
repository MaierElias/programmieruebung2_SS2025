import json
import pandas as pd
import plotly.express as px

from person import Person
# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])
        self.df = self.df.iloc[:5000]  # Entferne die erste Zeile, da sie nur die Spaltennamen enthält

    @staticmethod
    def load_by_id(input_persons, test_id):
        """
        Diese Funktion lädt den EKG-Test anhand der ID und der Personen-Datenbank.
        """
        input_persons = Person.load_person_data()
        for person in input_persons:
            for ekg_test in person["ekg_tests"]:
                if ekg_test["id"] == test_id:
                    return ekg_test
    
    def find_peaks(self, threshold=340):
        """
        a function that finds R-peaks in an EKG signal.
        """

        list_of_peaks = []	

        for index, row in self.df.iterrows():   
            if index == self.df.index.max():
                break 

            current_value = row['Messwerte in mV']

            # ist der current_value größer als der Vorgänger und Nachfolger
            if current_value > self.df.iloc[index-1]["Messwerte in mV"] and current_value >= self.df.iloc[index+1]["Messwerte in mV"]:
                #print("Found a peak at index: ", index)
                if current_value > threshold:
                    list_of_peaks.append(index)
        return list_of_peaks

    def plot_time_series(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        return self.fig 


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
    test_ekg = EKGdata(ekg_dict)
    test_ekg.plot_time_series().show(renderer="browser")
