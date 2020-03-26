#STRING FOR PyPOLL CHALLENGE

import csv

election_data=('election_data.csv')


#lists for financial analysis 
total_votes = 0         #total number of votes cast
list_candidates = []    #list of candidate names, with repetition of names
candidate_counter = {}  #dictionary for number of votes per candidate
candidate_info = {}     #dictionary for info of each candidate


with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)  
    
    for row in csvreader:
        
        #calculate total number of votes
        voter_id=row[0]
        total_votes += 1  
    
        #populate candidate list
        candidate=row[2]
        list_candidates.append(candidate)
        
    for candidate in list_candidates:
        if candidate not in candidate_counter:
            candidate_counter[candidate]=1
        else:
            candidate_counter[candidate] += 1
    
  
    #extrapolate winner
    max_vote = max(candidate_counter.values())
    for candidate in candidate_counter:
        if candidate_counter[candidate] == max_vote:
            winner= candidate


    #DEFINE RESULTS "BLOCK"
    s=""
    s+="Election Results\n"
    s+="-----------------------------------\n"
    s+=f'Total votes: {total_votes}\n'
    s+="-----------------------------------\n"
    for i in candidate_counter:
        vote = candidate_counter[i]
        perc = round(vote/total_votes*100,4)
        s += f"{i}: {perc}% ({vote})\n"
    s+="-----------------------------------\n"
    s+=f'Winner: {winner}\n'
    
    #PRINT RESULTS TO TERMINAL
    print(s)
        
    

#GENERATE OUTPUT FILE
#output file path
results=('Election_Results.txt')

with open(results, 'w', newline='\n') as text:

    text.write(s)





   