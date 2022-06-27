# the data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on populate vote. 

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Vote Counter
total_votes = 0

# Candidate Names list [] 
candidate_option = []

# Candidate votes dictionary {}
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)

    # Print each row in the CSV file. 
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # If statement to check if candidate does not match any existing candidate.
        if candidate_name not in candidate_option:

            # Add to list of candidates.
            candidate_option.append(candidate_name)

            # Track candidates vote count
            candidate_votes[candidate_name] = 0

        # Add vote to candidates vote count
        candidate_votes[candidate_name] += 1

# Save the results to text file.
with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")

    print(election_results, end="")

    # Save final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =

            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  print out the winning candidate, vote count and percentage to terminal.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    #print(winning_candidate_summary)
