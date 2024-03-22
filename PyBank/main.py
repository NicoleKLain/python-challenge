import csv #import csv module 

#set the filepath
filepath = "python-challenge/PyBank/Resources/budget_data.csv"
#Use csv module to to read a csv file 
with open(filepath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Prepare of variables 
    count_month = 0
    net_totalamount = 0
    amount_change = 0
    profit_loss_previous = 0
    greatest_increase = float('-inf')
    greatest_decrease = float('inf')
    greatest_increase_date = ""
    greatest_decrease_date = ""

    header = next(csv_reader)  # This is to exclude header from counting

#iterating through a CSV file and updating the count_month and net_totalamount variables
    for row in csv_reader:
        count_month += 1
        net_totalamount += int(row[1])

#calculate the current profit loss and the change in profit 
        profit_loss_current = int(row[1])
        if count_month > 1:
            change = profit_loss_current - profit_loss_previous
            amount_change += change
#find the greatest increase date
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
#find the greatest decrease date 
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        profit_loss_previous = profit_loss_current

    average_change = amount_change / (count_month - 1) if count_month > 1 else 0

print("Total Months:", count_month)
print("Total: $" + str(net_totalamount))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits:", greatest_increase_date, "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:", greatest_decrease_date, "($" + str(greatest_decrease) + ")")


#set the output filepath
output_file = "DataClass/python-challenge/PyBank/output_file.txt"

# Write the results to a text file
with open(output_file, "w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("-----------------------------\n")
        output_file.write(f"Total Months: {count_month}\n")
        output_file.write(f"Total: ${net_totalamount}\n")
        output_file.write(f"Average Change: ${round(average_change, 2)}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Financial analysis results have been written to output.txt")




