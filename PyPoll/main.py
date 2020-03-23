import csv

election_data=('election_data_file.csv')

#lists for financial analysis 
total_votes = 0         #total number of votes cast
list_candidates = []    #list of candidate names, with repetition of names
candidate_counter = {}  #dictionary for number of votes per candidate
winner="No one"

with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)  
    #print(csv_header)

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
    max_vote=max(candidate_counter.values())
    for candidate in candidate_counter:
        if candidate_counter[candidate] == max_vote:
            winner= candidate


    #PRINT TO TERMINAL
    print("-----------------------------------")
    print("Election Results")
    print("-----------------------------------")
    print(f'Total votes: {total_votes}')
    print("-----------------------------------")
    for i in candidate_counter:
        print(f'{i}: {float(round(candidate_counter[i]/total_votes*100,4))}% ({candidate_counter[i]})')
    print("-----------------------------------")
    print(f'Winner: {winner}')

#GENERATE OUTPUT FILE
results=('Election_Results.txt')

with open(results, 'w', newline='\n') as text:

    text.write("Election Results\n")
    text.write("-----------------------------------\n")
    text.write(f'Total votes: {total_votes}\n')
    text.write("-----------------------------------\n")
    for i in candidate_counter:
        text.write(f'{i}: {float(round(candidate_counter[i]/total_votes*100,4))}% ({candidate_counter[i]})\n')
    text.write("-----------------------------------\n")
    text.write(f'Winner: {winner}')




   