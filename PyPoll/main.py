# # Given a set of poll data called election_data.csv
# # Header Row: Voter ID, County, Candidate

# # Analyze the votes and calculate the following:
# #   The total number of votes cast
# #   A complete list of candidates who received votes
# #   The percentage of votes each candidate won
# #   The total number of votes each candidate won
# #   The winner of the election based on popular vote.

# Import Modules
import os
import csv

# Create path for data file with proper formatting for the operating system
csvpath = os.path.join('.','Resources','election_data.csv')
output_path = os.path.join('.','analysis','election_data_analysis.txt')
#print(csvpath)

# Initialize variables
vote_total = 0
candidates = []
total_candidate_votes = []

# open csv file as read only
with open(csvpath) as csvfile:

    # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each line of the CSV file
    for line in csvreader:
        # Calculate The total number of votes cast
        vote_total = vote_total + 1

        # A complete list of candidates who received votes
        if not(line[2] in candidates):
            candidates.append(line[2])
            total_candidate_votes.append(1)
        else:
            for x in range(len(candidates)):
                if line[2] == candidates[x]:
                    # Calculate The total number of votes each candidate won
                    total_candidate_votes[x] = total_candidate_votes[x] + 1
                    break
                x = x + 1

# As an example, your analysis should look similar to the one below:
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# Print the analysis to the terminal 
print(f"""
    Election Results
    -------------------------
    Total Votes: {vote_total}
    -------------------------""")
for x in range(len(candidates)):
    # Calculate The percentage of votes each candidate won
    candidate_percent = int(total_candidate_votes[x])/vote_total

    print(f"""    {candidates[x]}: {"{:.3%}".format(candidate_percent)} ({total_candidate_votes[x]})""")

# Calculate The winner of the election based on popular vote.
winner = candidates[total_candidate_votes.index(max(total_candidate_votes))]
print(f"""    -------------------------
    Winner: {winner}
    -------------------------""")

# Export a text file with the analysis results.