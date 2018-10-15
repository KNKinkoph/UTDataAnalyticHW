#PYPOLL

#Dependencies
import os
import csv

#File Path
PyPoll = os.path.join("election_data.csv")

#list to hold all unique candidates
candidates_options = []
#dictionary to track candidates and their corresponding votes: dictionaries will total like values by name: total count of votes by candidate name
candidate_votes = {}

with open("election_data.csv") as poll_data:
    #Dict reader returns an iterator that produces each row as needed we need to parse from here to get the data
    reader = csv.DictReader(poll_data)
    for row in reader:
        candidate_name = row["Candidate"]
        #creating a dictionary entry on the first occurence of candidate name
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
        #if candidate name already in candidate_votes, increment vote by 1
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
print(candidate_options)

        #Questions
        #Total number of votes cast
        #A complete list of candidates who received votes
        #the percentage of votes each candidate won
        #the total number ofvotes each candidate won
        #The winner of the election based on popular vote

 