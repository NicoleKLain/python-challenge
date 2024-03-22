import csv #import csv module 

#set the filepath
filepath = "python-challenge/PyPoll/Resources/election_data.csv"

#prepare the variables below as integer, list, and dictionary 
total_votecount= 0
candidates_list = []
candidate_votes = {}

#Use csv module to to read a csv file 
with open(filepath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader) #Exclude the header from counting
    
    #Iterate through the CSV data to extract the candidate names
    for row in csv_reader:
        total_votecount += 1
        candidate_name = row[2]
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votecount}")
print("-------------------------")

#Iterate the candidate votes and calculate the # of votes each candidate received

for candidate in candidates_list:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votecount) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
winner = max(candidate_votes, key=candidate_votes.get)
winning_votes = candidate_votes[winner]
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#set the textfile path 
outputfile = "DataClass/python-challenge/PyPoll/election_results.txt"

# Write the election results data to a text file

with open(outputfile, "w") as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {total_votecount}\n")
    outputfile.write("-------------------------\n")

    for candidate in candidates_list:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votecount) * 100
        outputfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    winner = max(candidate_votes, key=candidate_votes.get)
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-------------------------\n")

print("Election results have been written to 'election_results.txt'.")