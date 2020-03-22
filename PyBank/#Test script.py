#Test script
import csv

budget_data=('budget_data.csv')
# budget_data= 'C:/Users/Lorenza/DATA Science/nu-chi-data-pt-03-2020-u-c/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'



with open(budget_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #find header
    csv_header=next(csvreader)
    #print(f'CSV Header: {csv_header}')
    
    for row in csvreader:
            date = str(row[0])
            profit_losses = int(row[1])
            if date == "Jan-2010":
                print(date)
                print(profit_losses)


#THIS WORKS
with open(budget_origin, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #find header
    csv_header=next(csvreader)
    

    budget_origin = (csvreader)
    total_months = [months for months in budget_origin]
    print(f'Total Months: {int(len(total_months))}')

    #STILL NEED TO WORK ON THIS
    profit_losses = [row for row in budget_origin]
    print(profit_losses)
    # net_total = [profit_losses for profit_losses in (total_months[1])]
    # print(f'Total: ${net_total}')