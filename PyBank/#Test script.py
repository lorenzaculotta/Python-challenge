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

#---------------------------------------------------------------------------#
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

#---------------------------------------------------------------------------#
    
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

#---------------------------------------------------------------------------#
#MAX&MIN online
# function to find minimum and maximum position in list 
def min_and_max(a, n): 
  
    # inbuilt function to find the position of minimum  
    min_index = a.index(min(a)) 
      
    # inbuilt function to find the position of maximum  
    max_index = a.index(max(a))  
      
    # printing the position  
    print("The maximum is at position", maxpos + 1)
    print("The minimum is at position", minpos + 1)
      
#---------------------------------------------------------------------------#      
# driver code 
a = [3, 4, 1, 3, 4, 5]  
minimum(a, len(a)) 


        #find max
        for greatest_increase in csvreader:
            if greatest_increase > profit_losses:
                print(greatest_increase)
        greatest_decrease = min(enumerate(profit_losses))


#---------------------------------------------------------------------------#
#WORK IN PROGRESS FOR MAX AS LIST COMPREHENSION   
    max_profit_index= [profit for profit in enumerate(list_profit_losses) if profit == max_profit]
    print(max_profit_index)

#FAST WAY TO GET MAX  
#from this found online: a.index(max(a))  
    max_idx= list_profit_losses.index(max(list_profit_losses))
    print(total_months[max_idx])


#---------------------------------------------------------------------------#
#FIND MAX WORKS!!!  
   max_profit = max(list_profit_losses)
    for index,profit in enumerate(list_profit_losses):
        if profit == max_profit:
            print(index,profit)
            print(f'Greatest Increase: {total_months[index]} (${max_profit})')