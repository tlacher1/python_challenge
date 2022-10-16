#import mods
import csv
import os
import collections as ct

#setting path of file to read
election_data = os.path.join("Resources","election_data.csv")

#setting lists
candidate= []
winner_list = []
votes = ct.Counter()

#setting variables
alpha_first  = 0
alpha_second = 0
alpha_third = 0
vote_count = 0
winner = ''

#opening csv file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_file)

    #Loop through file
    for row in csv_reader:
        #Counting total number of votes and storing candidate information
        vote_count = vote_count +1            
        candidate= row[-1]
        votes[candidate] += 1
        #Finding winner's name
        winner_list = (votes.most_common(1))
        winner = winner_list[0]

        #Getting sorted candidate names and their total vote values
        sorted_value = list(votes.values())
        sorted_keys = list(votes.keys())

#Calculating percentages for candidates
alpha_first = (int(sorted_value[0])/int(vote_count))*100
alpha_second = (int(sorted_value[1])/int(vote_count))*100
alpha_third = (int(sorted_value[2])/int(vote_count))*100


#Printing off stored values
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
print(f"{(sorted_keys[0])}: {alpha_first:.3f}% ({sorted_value[0]})")
print(f"{(sorted_keys[1])}: {alpha_second:.3f}% ({sorted_value[1]})")
print(f"{(sorted_keys[2])}: {alpha_third:.3f}% ({sorted_value[2]})")
print("----------------------------")
print(f"Winner: {winner[0]}")
print("----------------------------")

#setting output file to write to
with open("election_analysis.txt","w") as text:
    text.write("Election Results" "\n")
    text.write("----------------------------\n")
    text.write(f"Total Votes: {vote_count}\n")
    text.write("----------------------------\n")
    text.write(f"{(sorted_keys[0])}: {alpha_first:.3f}% ({sorted_value[0]})\n")
    text.write(f"{(sorted_keys[1])}: {alpha_second:.3f}% ({sorted_value[1]})\n")
    text.write(f"{(sorted_keys[2])}: {alpha_third:.3f}% ({sorted_value[2]})\n")
    text.write("----------------------------\n")
    text.write(f"Winner: {winner[0]}\n")
    text.write("----------------------------\n")
