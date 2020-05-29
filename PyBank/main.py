# This is a Python script for analyzing the financial records of your company. 
# Set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 

# Import Modules
import os
import csv

# Create path for data file with proper formatting for the operating system
csvpath = os.path.join('.','Resources','budget_data.csv')
output_path = os.path.join('.','analysis','budget_data_analysis.txt')
#print(csvpath)

# Initialize variables
num_months = 0
net_total = 0
avg_change = 0
last_month = 0
change = 0
net_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# open csv file as read only
with open(csvpath) as csvfile:

    # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each line of the CSV file
    for line in csvreader:
        #print(f"{csvreader.line_num} {line}")
        if csvreader.line_num == 2:
            last_month = int(line[1])
        # Calculate the total number of months included in the dataset
        num_months = num_months + 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(line[1])

        # Calculate change from last month
        #print(f"net_change = {net_change}")
        change = int(line[1]) - last_month
        #print(f"change = {change}")
        net_change = net_change + change
        #print(f"net_change = {net_change}")
        
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period
        if greatest_increase < change:
            greatest_increase = change
            greatest_increase_month = line[0]
        elif greatest_decrease > change:
            greatest_decrease = change
            greatest_decrease_month = line[0]

        # Store this month's value in last_month for next month's change calculation
        last_month = int(line[1])

    #print(f"net_change = {net_change}")
    # The average of the changes in "Profit/Losses" over the entire period
    avg_change = round(net_change / (num_months - 1),2)

# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Print the analysis to the terminal 
print(f"""
    Financial Analysis
    ----------------------------
    Total Months: {num_months}
    Total: ${net_total}
    Average Change: ${avg_change}
    Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
""")

# Export a text file with the results.
