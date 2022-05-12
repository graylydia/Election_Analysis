#The Data we need to retrieve.

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare new list for Candidate options
candidate_options = []
# Declare new dictionary for candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
           
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
       
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print out the winning candidate, vote count, and percentage to terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Print the total votes. 
#print(total_votes)
# Print the candidates
#print(candidate_options)
# Print the candidate vote dictionary.
#print(candidate_votes)

    
    # Retrieve the first item from each row
    #for row in file_reader:
     #   print(row[0])


    # Print the file object.
    #print(election_data)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as text_file:

    # Write some data to the file.
    #text_file.write("Counties in the Elextion\n-----------------\nArapahoe\nDenver\nJefferson")


# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: perform analysis.
    #print(election_data) 

    # filereader = csv.reader(election_data)
    #print(filereader)
    #for r in filereader:
     #   print(r)



# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.