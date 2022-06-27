# the data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on populate vote. 

# import csv

# # Assign variable for file to load 
# file_to_load = 'Resources/election_results.csv'

# # Open election results and read the file
# with open(file_to_load) as election_data:

# # To do: perform analysis.
#     print(election_data)


# import csv
# import os

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)


# import csv
# import os

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file. 
# # outfile = open(file_to_save, "w")

# # Use the with statement to open file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write data to the file
#     txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")
    
# # Close the file if you use the open statment. Do not need close statment when using WITH statment to open file.
# # outfile.close()



# Add our dependencies.
import csv
from email import header
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

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# # Print the total votes.
# print(candidate_votes)
