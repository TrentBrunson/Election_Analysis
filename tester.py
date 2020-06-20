import csv
import os

dir(csv)
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

#Open the data file.
fileLoad = os.path.join("Resources", "election_results.csv")

with open(fileLoad) as electionData:
    print(electionData)

print(dir)

counties = ['Arapahoe', 'Denver', 'Jefferson', 'El Paso']

print(counties)

counties.append('El Paso')

counties.append('el paso')

print(counties)

#C:\Users\bbiz2\dataAustin2020\Election_Analysis\Resources\election_results.csv

