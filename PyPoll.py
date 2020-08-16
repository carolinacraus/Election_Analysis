import csv
import os

# The data we need to retrieve
# assign a variable for the file to load and the path 
file_load= os.path.join("Resources\election_results.csv")
file_save = os.path.join("Analysis", "election_analysis.txt")

# open election results and read file 
#election_data = open(f, 'r')
with open(file_load) as election_data: 
    #print(election_data)
    reader = csv.reader(election_data)

    # read the file object with the reader function 
    headers = next(reader)
    # print header row 
    print(headers)
    #for row in reader:
        #print(row)

# open output file as a text file
with open(file_save, "w") as txt_file:
    # write some data to the file
    txt_file.write("hello world")

# initialize total vote counter


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote 

# close file 
 
