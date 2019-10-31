import csv

csvpath = "Resources/budget_data.csv"

totalMonths = 0
totalProfit = 0
greatestMonth = ""
greatestAmount = 0
worstMonth = ""
WorstAmount = 0
lastMonth = 0
monthlyChange = 0
totalChange = 0
avgCount = 0
avgChange = 0

with open(csvpath, newline='') as csvfile:

    budgetData = csv.reader(csvfile, delimiter=',')

    csv_header = next(budgetData)
    

    for row in budgetData:
        totalMonths += 1
        totalProfit += float(row[1])

        if(lastMonth != 0):
            monthlyChange = float(row[1]) - lastMonth 
            avgCount += 1
            totalChange += monthlyChange    
    
        if(greatestAmount != 0):
            if(greatestAmount < (float(row[1]) - lastMonth)):
                greatestAmount = float(row[1]) - lastMonth
                greatestMonth = row[0]
        else:
            greatestAmount = float(row[1]) - lastMonth
            greatestMonth = row[0]

        if(WorstAmount != 0):
            if(WorstAmount > (float(row[1]) - lastMonth)):
                WorstAmount = float(row[1]) - lastMonth
                worstMonth = row[0]
        else:
            WorstAmount = float(row[1]) - lastMonth
            worstMonth = row[0]

        lastMonth =  float(row[1])



    avgChange = round(totalChange/avgCount, 2)

with open("output.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write("Total Months: " + str(totalMonths) + "\n")
    output_file.write("Total: $" + str(round(totalProfit, 2)) + "\n")
    output_file.write("Average Change: $" + str(round(avgChange, 2)) + "\n")
    output_file.write("Greatest Increase in Profits: " + str(greatestMonth) + " ($" + str(round(greatestAmount, 2)) + ")\n")
    output_file.write("Greatest Decrease in Profits: " + str(worstMonth) + " ($" + str(round(WorstAmount, 2)) + ")\n")
    output_file.close()

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(round(totalProfit, 2)))
print("Average Change: $" + str(round(avgChange, 2)))
print("Greatest Increase in Profits: " + str(greatestMonth) + " ($" + str(round(greatestAmount, 2)) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + " ($" + str(round(WorstAmount, 2)) + ")")


       