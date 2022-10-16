#import mods
import csv
import os

#setting path of file to read
budget_data = os.path.join("Resources","budget_data.csv")

#setting lists
profits= []
monthly_change = []
date = []

#setting variables
month_count = 0
total_profits = 0
initial_profit = 0
greatest_increase = 0
greatest_decrease = 0
greatest_date = ''
lowest_date = ''


#opening csv file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_file)
    
    #Loop through file
    for row in csv_reader:
        #Counting total number of months
        month_count = month_count +1

        #Gathering date information into list
        date.append(row[0])
        
        #Sum total revenue for the period and create a list for of profits
        profits.append(row[1])
        total_profits = total_profits + int(row[1])

        #Gathering the profit / loss changes for the entire period
        final = int(row[1]) - initial_profit
        initial_profit = int(row[1])

        monthly_change = monthly_change + [final]
        
        #Calculating the average of the P/L changes
        average = sum(monthly_change)/month_count

        #find the greatest increase 
        greatest_increase = max([int(i) for i in profits])
        greatest_date = date[profits.index(str(greatest_increase))]

        #find the greatest decrease 
        greatest_decrease =  min([int(i) for i in profits])
        lowest_date = date[profits.index(str(greatest_decrease))]

#Printing off stored values
print("Financial Analysis")
print ("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})")

#setting output file to write to
with open("budget_analysis.txt","w") as text:
    text.write("Financial Analysis" "\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {month_count} \n")
    text.write(f"Total: ${total_profits} \n")
    text.write(f"Average Change: ${average:.2f} \n")
    text.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase}) \n")
    text.write(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease}) \n")