# Add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

#declarations
total_votes = 0 #set vote counter
county_total_votes = 0 #set county vote counter
candidate_options = [] #declaring list to hold list of candidates
candidate_votes = {} #delcaring dictionary where 'candidate name' is 'key', and 'votes' is 'value'
county_votes = {} #decalring dictionary where 'county name' is key and 'votes' is value
county_options = [] #declaring list to hold list of counties
largest_county = "" #declaring string to hold the name county with largest total # of votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0
county_turnout = 0

#{'candidate_name1':votes, 'candidate_name2':votes, 'candidate_name3':votes}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader) #skip header row

    for row in file_reader:
        total_votes += 1 #2-add totals to vote count
        candidate_name = row[2] #print candidate name for each row
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) #add candidate name to cadidate list
            candidate_votes[candidate_name] = 0 #begin tracking the candidate's vote count
            
        candidate_votes[candidate_name] += 1 #looping thru rows and incrementing candidate votes in dictionary each time name is seen

        county_total_votes += 1 #increment vote count per county
        county_name = row[1]
        if county_name not in county_options: #if it comes across something not in the list, do:
            county_options.append(county_name) #add newly found value to the list
            county_votes[county_name] = 0 #intialize vote counter by county
        
        county_votes[county_name] += 1 #in each row that it finds the county name, increment the vote total for that county

for candidate in candidate_votes:
    votes = candidate_votes[candidate] #retrieve vote count of candidate
    vote_percentage = int(votes)/int(total_votes)*100

    #report the winning candidate name, vote totals and percentage
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_percentage = vote_percentage
        winning_count = votes
        winning_candidate = candidate


# Using the with statement to open the file as a text file.
with open(file_to_save, "w") as textFile:

    # Write some data to the file and screen
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    textFile.write(election_results)  #save the final vote count to the text file.

    print(f'\nCounty Votes:\n',end="") 
    textFile.write(f'\nCounty Votes:\n')

    #printing to screen vote totals by county
    for county in county_votes:   
        c_votes = county_votes[county] #get the vote totals for each county
        county_percentage = int(c_votes) / int(county_total_votes)*100
    
        if (c_votes > county_turnout):
            county_turnout = c_votes
            largest_county = county
     
        county_results = (f'{county}: {county_percentage:.1f}% ({c_votes:,})\n')
        print(county_results, end="") #print(f'{county_results}\n') 
        textFile.write(county_results)
    
    largest_county_summary = (
        f'\n-------------------------\n'
        f'Largest County Turnout: {largest_county}\n'
        f'-------------------------\n'
    )
    print(largest_county_summary)
    textFile.write(largest_county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")        
        print(candidate_results) #print each candidate's voter count and percentage to the terminal.
        textFile.write(candidate_results) #save candidate results to text file

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary) 
    # Save the winning candidate's results to the text file.
    textFile.write(winning_candidate_summary)
