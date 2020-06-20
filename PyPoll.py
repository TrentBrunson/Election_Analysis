# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as textFile:

    # Write some data to the file.
    textFile.write("Counties in the Election\n------------------------\n")
    # Write three counties to the file.
    textFile.write("Arapahoe\nDenver\nJefferson")





#C:\Users\bbiz2\dataAustin2020\Election_Analysis\Resources\election_results.csv
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.