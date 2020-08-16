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
winning_count = 0 
winning_percentage = 0

# open election results and read file 
#election_data = open(f, 'r')
with open(file_load) as election_data: 
    #print(election_data)
    reader = csv.reader(election_data)

    # read the file object with the reader function 
    headers = next(reader)

    # increment total votes by iterating through file rows 
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

 # save results to a text file        
with open(file_save, "w") as txt_file: 
    # print the final vote count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save final vote count to text file 
    txt_file.write(election_results)

    # determine percentage of votes for each candidate by looping through counts
    # iterate through candidate list 
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100 

        # print out each candidate name, vote count, & votes to terminal 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # save candidate results to text file 
        txt_file.write(candidate_results)
        # determine winning count and candidate 
        # determine if votes is greater than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, winning_count = votes  & winning_percentage = votes_percentage 
            winning_count = votes
            winning_percentage = vote_percentage
            # set winning candidate wo candidate name 
            winning_candidate = candidate_name 
    # determine winning vote count
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's results to the text file 
    txt_file.write(winning_candidate_summary)
  
        

#print(total_votes)
#print(candidate_options)
#print(candidate_votes) 


# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote 

# close file 
 