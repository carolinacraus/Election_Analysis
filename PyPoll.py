import csv
import os

# The data we need to retrieve
# assign a variable for the file to load and the path 
file_load= os.path.join("Resources\election_results.csv")
file_save = os.path.join("Analysis", "election_analysis.txt")

# Inititalie variable for total number of votes cast 
total_votes = 0

# list to hold candidate options 
candidate_options = [] 

# declare empty dictionary to hold candidate votes
candidate_votes = {} 

# winning candidate and winning count tracker 
winning_candidate = ''
winning count = 0 
winning_percentage = 0


# open election results and read file 
#election_data = open(f, 'r')
with open(file_load) as election_data: 
    #print(election_data)
    reader = csv.reader(election_data)

    # read the file object with the reader function 
    headers = next(reader)

    # print header row 
    #print(headers)
    for row in reader:
        total_votes += 1 
        #print(row)

        # candidate name from each row to list 
        candidate_name = row[2]
        # if candidate does not match any exisiting candidate 
        if candidate_name not in candidate_options: 
            # add to list of candidates
            candidate_options.append(candidate_name)

            # begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

        # determine winning vote count

print(total_votes)
print(candidate_options)
print(candidate_votes) 

# determine the percentage of votes for each candidate  by looping through the counts.
for candidate_name in candidate_votes: 
    # retrieve vote count for candidate
    votes = candidate_votes[candidate_name]
    # calculcate percentage of votes
    vote_percent = float(votes) / float(total_votes) * 100 
    #  Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percent}% of the vote.")

# open output file as a text file
with open(file_save, "w") as txt_file:
    # write some data to the file
    txt_file.write("hello world") 

# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote 

# close file 
 
