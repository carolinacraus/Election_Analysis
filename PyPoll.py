import csv
import os

# The data we need to retrieve
# assign a variable to load file from a path 
file_load= os.path.join("Resources\election_results.csv")
# add a variable to save file to a path 
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

# create a county list and county votes dictionary 
counties = [] 
county_votes = {} 

# track largest county and county voter turnout 
largest_county = ""
county_turnout = 0 

# open election results and read file 
#election_data = open(f, 'r')
with open(file_load) as election_data: 
    #print(election_data)
    reader = csv.reader(election_data)

    # read the file object with the reader function 
    headers = next(reader)

    # increment total votes by iterating through file rows 
    for row in reader:
        # add to total vote count 
        total_votes += 1 

        # candidate name from each row to list 
        candidate_name = row[2]

        # extract the county name from each row 
        county_name = row[1]
        
        # if candidate does not match any exisiting candidate 
        if candidate_name not in candidate_options: 
            # add to list of candidates
            candidate_options.append(candidate_name)

            # begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1

        # if county does not match any existing county in county list 
        if county_name not in counties: 
            # add existing county to list of counties 
            counties.append(county_name)

            # begin tracking that county's vote count 
            county_votes[county_name] = 0
        
        # add vote to that county's count 
        county_votes[county_name] += 1 
    # print each candidate's voter count and percentage to terminal
    print(county_turnout)

# save results to a text file        
with open(file_save, "w") as txt_file: 
    # print the final vote count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # save final vote count to text file 
    txt_file.write(election_results)

    # write a repetition statement to get the county from the county votes dictionary
    for county_name in county_votes: 
        # retrieve the vote count 
        votes= county_votes[county_name]
        # calculate percent of total votes for the county 
        vote_percent = float(votes) / float(total_votes) * 100 

        # print out each county results to terminal 
        county_results = (
            f"{county_name}: {vote_percent:.1f}% ({votes:,})\n")
        print(county_results)
        # save candidate's results to text file 
        txt_file.write(county_results)

        # write a decision statement that determine the county with the largest vote count
        if (votes> winning_count) and (vote_percent > winning_percentage):
            winning_count = votes
            largest_county = county_name
        largest_county = (
          f"\n-------------------------"  
          f"Largest County Turnout: {largest_county}"
          f"-------------------------\n"
        )
       

      
    # determine percentage of votes for each candidate by looping through counts
    # iterate through candidate list 
    for candidate_name in candidate_votes:
        # retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]

        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100 

        # print out each candidate name, vote count, & votes to terminal 
        candidate_results = (f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
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
    # print winning candididates to terminal 
    winning_candidate_summary = (
        f"\n-------------------------\n"
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
 