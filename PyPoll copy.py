# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = os.path.join("analysis", "election_results.txt")

#declarations
total_votes = 0 #set vote counter
candidate_options = [] #declaring list to hold list of candidates
candidate_votes = {} #delcaring dictionary where 'candidate name' is 'key', and 'votes' is 'value'
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#{'candidate_name1':votes, 'candidate_name2':votes, 'candidate_name3':votes}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes +=1 #2-add totals to vote count
        candidate_name = row[2] #print candidate name for each row
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) #add candidate name to cadidate list
            candidate_votes[candidate_name] = 0 #begin tracking the candidate's vote count
            
        candidate_votes[candidate_name] += 1 #looping thru rows and incrementing candidate votes in dictionary each time name is seen

for candidate in candidate_votes:
    votes = candidate_votes[candidate] #retrieve vote count of candidate
    vote_percentage = int(votes)/int(total_votes)*100
    print()
    print(f'{candidate} received {vote_percentage:.1f}% of the vote.')

    #report the winning candidate name, vote totals and percentage
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_percentage = vote_percentage
        winning_count = votes
        winning_candidate = candidate

#winning_candidate_summary = (
    #f"---------------------------\n"
    #f"Winner: {winning_candidate}\n"
    #f"Winning Vote Count: {winning_count:,}\n"
    #f"Winning Percentage: {winning_percentage:.1f}%\n"
    #f"---------------------------\n")
#print(winning_candidate_summary)


#print(candidate_votes)
#print(vote_percentage)

# Using the with statement to open the file as a text file.
with open(file_to_save, "w") as textFile:

    # Write some data to the file.
    textFile.write("Counties in the Election\n------------------------\n")
    # Write three counties to the file.
    textFile.write("Arapahoe\nDenver\nJefferson\n")
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    textFile.write(election_results)  #save the final vote count to the text file.


    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")        
        print(candidate_results) #print each candidate's voter count and percentage to the terminal.
        textFile.write(candidate_results) #save  candidate results to text file
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


#C:\Users\bbiz2\dataAustin2020\Election_Analysis\Resources\election_results.csv
#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.