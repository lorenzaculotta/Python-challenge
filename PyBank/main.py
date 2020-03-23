#NOTE: In addition, your final script should both print the analysis to the terminal 
#and export a text file with the results.

import csv

budget_origin=('budget_data.csv')

#lists for financial analysis (NEEDED IN VERSION WITHOUT COMPREHENSION)
total_months = []       #total number of months included in the dataset   NOT NEEDED
net_total = 0          #net total amount of "Profit/Losses" over the entire period
list_profit_losses = []
#NOT NEEDED average_change = []     #average of the changes in "Profit/Losses" over the entire period
#NOT NEEDED greatest_increase = []  #greatest increase in profits (date and amount) over the entire period
#NOT NEEDED greatest_decrease = []  #greatest decrease in losses (date and amount) over the entire period




with open(budget_origin, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #find header
    csv_header=next(csvreader)
    #print(f'CSV Header: {csv_header}')
    
    for row in csvreader:
        date=row[0]
        total_months.append(date)
      
        profit_losses = row[1]
        list_profit_losses.append(int(profit_losses))
    
        net_total += int(profit_losses)
        
    #calculate average change
    avg_change= round(net_total / len(total_months),2)
    
    #find greatest increase
    max_profit = max(list_profit_losses)
    max_index = list_profit_losses.index(max(list_profit_losses))
    
    #find greatest decrease
    min_profit = min(list_profit_losses)
    min_index = list_profit_losses.index(min(list_profit_losses))
    


       
    print(f'Total Months: {int(len(total_months))}')
    print(f'Total: ${int(net_total)}')
    print(f'Average Change: {avg_change}')
    print(f'Greatest Increase: {total_months[max_index]} (${max_profit})')
    print(f'Greatest Decrease: {total_months[min_index]} (${min_profit})')

