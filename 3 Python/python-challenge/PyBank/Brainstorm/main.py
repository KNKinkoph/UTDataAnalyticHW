##PYBANK
#Dependencies
import os
import csv

#name file path, changed profit/loss column to "revenue" for easier understanding
PyBank = os.path.join("budget_data.csv")

#open lists that will be totaled later / greatest increase/decrease the numeric values is what we are comparing to
#99999999 because they may always make a profit and are never at 0, make a large number to compare to
#Create Lists
prev_revenue = 0 
revenue_change_list = []
total_revenue = 0
total_months = 0
avg_revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

# with open csv file (budet_data) as csvfile:
with open("budget_data.csv") as revenue_data:
    reader = csv.DictReader(revenue_data)
    for row in reader:
        #calculate total months
        total_months = total_months + 1

        #calculate total revenue, index for profit/loss is 1
        total_revenue = total_revenue + float(row["Revenue"])

        #calculate revenue change
        #defining revenue change/ previous revenue starting value is 0 because there is nothing that has come before it but it needs a value
        revenue_change = int(row["Revenue"]) - prev_revenue 

        #call append function to add revnue_change to revenue_change_list
        revenue_change_list.append(revenue_change)

        # prepare previous revenue for the next iteration
        prev_revenue = int(row["Revenue"])

        #if revenue change is greater than the current record holder for greatest revenue 
        #rewrite the greatest revenue - rewriting highest score
        if (revenue_change > int(greatest_increase[1])):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

#to get the average revenue change, you will take the sum of the items we added to the revenue change list and divide by the count aka len of the revenue change list
avg_revenue_change = sum(revenue_change_list) / len(revenue_change_list)

#cleaner way of printing the values of each is by creating f strings to print the variable values \n is to start new line
output = (
    f"Financial Analysis: \n"
    f"Total Months: {total_months} \n"
    f"Total Revenue: {total_revenue} \n"
    f"Average Revenue Change: {avg_revenue_change} \n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]}) \n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})"
)
print("--------")
print(output)
print("--------")

# writing text file with f strings

with open("Output.txt", "w") as outfile:
    outfile.write(output)