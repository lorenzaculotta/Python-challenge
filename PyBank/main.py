#STRING FOR PyBANK CHALLENGE

import csv

budget_origin=('budget_data.csv')

#lists for financial analysis
total_months = []       #total number of months included in the dataset
total_net = 0           #net total amount of "Profit/Losses" over the entire period
list_profits = []       #list of profit/losses values
list_changes = []       #list changes in "Profit/Losses" over the entire period

with open(budget_origin, 'r', newline='\n') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #find header
    csv_header=next(csvreader)
    
    #populate list of months and list of profits/losses
    for row in csvreader:
        date=row[0]
        total_months.append(date)
      
        profits = row[1]
        list_profits.append(int(profits))
        
        #calculate net total
        total_net += int(profits)

    #calculate changes from one month to another and populate list of changes   
    for profits in list_profits:
        idx= list_profits.index(profits)
        change = int(list_profits[idx]) - int(list_profits[idx-1])
        list_changes.append(change)
        
  
    #calculate average change
    list_changes.pop(0)
    avg_change= round(sum(list_changes) / len(list_changes),2)

    #calculate greatest increase
    max_profit = max(list_changes)
    max_index = list_changes.index(max(list_changes)) +1

    
    #calculate greatest decrease
    min_profit = min(list_changes)
    min_index = list_changes.index(min(list_changes)) +1
    
    #DEFINE RESULTS "BLOCK"
    s= ""
    s+="Financial Analysis\n"
    s+="-----------------------------------\n"
    s+=f'Total Months: {int(len(total_months))}\n'
    s+=f'Total: ${int(total_net)}\n'
    s+=f'Average Change: ${avg_change}\n'
    s+=f'Greatest Increase in Profits: {total_months[max_index]} (${max_profit})\n'
    s+=f'Greatest Decrease in Profits: {total_months[min_index]} (${min_profit})\n'
        
    #PRINT RESULTS TO TERMINAL
    print(s)
    
#GENERATE OUTPUT FILE
#output file path
analysis=('Financial_Analysis.txt')

with open(analysis, 'w', newline='\n') as text:
    text.write(s)


