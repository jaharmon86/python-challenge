import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

months = []
total_months = len(months)
total_PL = []
revenue_change = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    for row in csvreader:
        months.append(row[0])
        total_PL.append(int(row[1]))

    for x in range(1, len(total_PL)):
        revenue_change.append(int(total_PL[x])-int(total_PL[x-1]))

revenue_average = sum(revenue_change) / len(revenue_change)

greatest_increase = max(revenue_change)
greatest_decrease = min(revenue_change)

#print(total_PL)
#print(


print("")
print("Financial Analysis")
print("----------------------------")
print("total months: " + str(len(months)))
print(f"Total: ${sum(total_PL)}")
#print("Total: " + "$")  print(sum(total_PL))
print("Average change: " + "$" + str(revenue_average))
print("Greatest Increase in Profits: " + str(months[revenue_change.index(greatest_increase)+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(greatest_decrease)+1]) + " " + "$" + str(greatest_decrease))

file = open("pybank.txt", "w")
file.write("Financial Analysis")
file.write("\n----------------------------")
file.write("\ntotal months: " + str(len(months)))
file.write("\n")
file.write(f"Total: ${sum(total_PL)}")
file.write("\nAverage change: " + "$" + str(revenue_average))
file.write("\nGreatest Increase in Profits: " + str(months[revenue_change.index(greatest_increase)+1]) + " " + "$" + str(greatest_increase))
file.write("\nGreatest Decrease in Profits: " + str(months[revenue_change.index(greatest_decrease)+1]) + " " + "$" + str(greatest_decrease))
file.close()

