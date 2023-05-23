import json
import csv

with open('Sourcefiles/analytics.json') as f:
    daten = json.load(f)

parametername = 'websiteUrl'
parameter_werte = [eintrag[parametername] for eintrag in daten]

with open('ergebnis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([parametername])
    writer.writerows(zip(parameter_werte))
