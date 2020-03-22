#NOTE: In addition, your final script should both print the analysis to the terminal 
#and export a text file with the results.

import csv

budget_origin=('budget_data.csv')

#lists for financial analysis (NEEDED IN VERSION WITHOUT COMPREHENSION)
total_months = []       #total number of months included in the dataset   NOT NEEDED
net_total = 0          #net total amount of "Profit/Losses" over the entire period
average_change = []     #average of the changes in "Profit/Losses" over the entire period
greatest_increase = []  #greatest increase in profits (date and amount) over the entire period
greatest_decrease = []  #greatest decrease in losses (date and amount) over the entire period




with open(budget_origin, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #find header
    csv_header=next(csvreader)
    #print(f'CSV Header: {csv_header}')
    
    for row in csvreader:
        date=row[0]
        total_months.append(date)
      
        profit_losses=int(row[1])
        net_total += profit_losses

    print(f'Total Months: {int(len(total_months))}')
    print(f'Total: ${int(net_total)}')










    # date=(csvreader[0])
    # total_months = [month for months in date]
    # print(total_months)
