# Programmierübung 2


## Ziel des Projekts
Erstellen einer Grafik, welche die sortierten Wattzahlen mit Hilfe von Matplotlib ausgiebt (Siehe unten).

## Ergebnisgrafik

![Power Curve](figures/power_curve.png)

## Umgang mit PDM

- Zum Aufsetzen dieses Projekts einmalig `pdm init`
- Zum Installieren dieses Projekts nach dem clonen `pdm install`
- Zum Hinzufügen eines Pakets `pdm add <packetname>`

- `.gitignore`legt fest, welche Dateien von git ignoriert werden. Hier muss __immer vor__ dem ersten Commit der Ordner `.venv/` drin stehen.

# EKG- Analyze App

## Funktionsumfang (Lastenheft)
- Die App ermöglicht die Analyse von EKG-Daten
- Dabei werden folgende Use-Cases unterstützt:

![alt text](docs/uml_usecase.svg)

### Funktionale Anforderungen

- [ ] Als Nutzer:in möchte ich eine Versuchsperson auswählen und die relevanten Daten angezeigt bekommen
- [ ] Als Nutzer:in möchte ich mir das Bild einer Versuchsperson anzeigen lassen, um mich zu vergewissern, dass ich die richtige Person anzeige (Termin 2)
- [ ] Als Nutzer:in möchte ich die zu einer Versuchsperson gehörenden EKG Datensätze auswählen können (sofern es mehrere gibt)
- [ ] Als Nutzer:in möchte ich die EKG-Daten einer Versuchsperson als Grafik anzeigen lassen (Termin 3)
- [ ] Als Nutzer:in möchte ich mir den Durchschnittspuls einer Versuchsperson als Zahl anzeigen lassen (Termin 4)