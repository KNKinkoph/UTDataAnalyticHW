#PYPOLL
#Dependencies

import os
import csv

from collections import Counter
#in order to use the counter you must import the collecitons 

#File Path
PyPoll = os.path.join("election_data.csv")

#list to hold all unique candidates
candidate_options = []
total_votes = 0 

#dictionary to track candidates and their corresponding votes: dictionaries will total like values by name: total count of votes by candidate name
candidate_votes = {}

with open("election_data.csv") as poll_data:
    #Dict reader returns an iterator that produces each row as needed we need to parse from here to get the data
    reader = csv.reader(poll_data)
    next(reader)
    for row in reader:
        #counting candidates
        candidate_options.append (row[2])
    #set candidate options to set or complete a different list
candidate_name = set(candidate_options)
name_count = Counter(candidate_options)
print("----------")

#total votes, len is a counter function of python
total_votes = len(candidate_options)
print(total_votes)

#% of votes each candidate won
for candidate_options, item in name_count.items():
    percent = round((item/total_votes*100),2)
    print(candidate_options  +  ": {0} %\n".format(percent))
    print("----------")
   
    
#winner
max_value = max(name_count.values())  # maximum value
max_keys = [k for k, v in name_count.items() if v == max_value] # getting all keys containing the `maximum`
print("Winner: ")
print(max_keys)
print("----------")


        #Questions
        ###Total number of votes cast
        ###A complete list of candidates who received votes
        #the percentage of votes each candidate won
            #ex: percent = round(int(row[6])/int(row[5]), 2) 
        #the total number of votes each candidate won
        #The winner of the election based on popular vote

#write text file - print statements?
with open("Output.txt", "w") as outfile:
    outfile.write(str(total_votes))
    outfile.write(candidate_options  +  ": {0} %\n".format(percent)) 
    outfile.write("Winner ")