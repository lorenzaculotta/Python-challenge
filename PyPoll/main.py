import csv

election_data=('election_data_file.csv')

#lists for financial analysis 
total_votes = 0         #total number of votes cast
list_candidates = []    #list of candidate names
candidate_counter = {}  #dictionary for number of votes per candidate
#percent = {}  #dictionary for percentage  



with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)  #WORKS
    #print(csv_header)

    for row in csvreader:
        
        #calculate total number of votes
        voter_id=row[0]
        total_votes += 1  #works!!!!
    
        #populate candidates list
        candidates=row[2]
        list_candidates.append(candidates)
        
    for candidates in list_candidates:
        if candidates not in candidate_counter:
            #candidate_counter.append(candidates)
            candidate_counter[candidates]=1
        else:
            candidate_counter[candidates] += 1

    # for candidates in candidate_counter:
    #     candidate_percent= candidate_counter[candidates] / total_votes *100
        

    for i in candidate_counter:
        print(f'{i}: {(round(candidate_counter[i]/total_votes*100},2))}% ({candidate_counter[i]})')
    




  
    
    #calculate number of votes for each candidate


    #print(candidate_counter)
    #print(total_votes) #works!!!


   