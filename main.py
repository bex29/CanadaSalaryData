# what do i want from this script? I wanna be able to get the canadian/provincial average salaries. Also, I wanna get the median data.
#also, filter based on the yrs of exp
import csv
import math
import statistics
# i just discovered the statistics module and apparently it could've made my life much easier with the the functions that calculate the average
# the good news is that I found the module early on and I'll use it for the median functions and change the range functions to give the range between
# low median and high median
def calculateTotalAverageCanada(csvFileInput):
    # Calculate the average salary from a CSV file of Canadian SDE incomes.
    # the input is a csv file
    # the output is an integer value of the canadian average
    with open(csvFileInput) as csvFile:
        csv_reader = csv.reader(csvFile)
        headers = next(csv_reader)  # Skip the header row
        total_salary = 0
        count = 0
        numberOfInputs = 0
        numberOfErrorInputs = 0
        print(csv_reader.line_num)
        for row in csv_reader:
            numberOfInputs += 1
            salaryField = row[4]
            salary_str = salaryField[1:].replace(",", "").split('.')[
                0]  # remove the dollar sign [1:] and replace the commas
            # and then get rid of whatever comes after the comma: split(".")[0]
            salary_str = row[4][1:].replace(",", "").split('.')[0]
            try:
                salary = int(salary_str)
                total_salary += salary
                count += 1
            except ValueError:
                numberOfErrorInputs += 1
                print(f"Unable to convert salary '{salary_str}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return int(total_salary / count) if count > 0 else 0


# Original function I wrote for the provincial average with original comments
# def calculateTotalAverageProvince(csvFileInput, provinceName):
#     #get the provincial averages, the inputs are the province abbreviations such as ON for Ontario, BC for British Columbia, etc. Check the csv file for more info
#     with open(csvFileInput) as csvFile:
#         csv_reader = csv.reader(csvFile, delimiter=",")
#         totalSalary = 0
#         countPerson = 0
#         for row in csv_reader:
#             if (provinceName.upper() in row[2]): # check the desired province against the province column
#                 salaryInt = row[4][1:].replace(",", "") #get the salary from the row and remove the comma from the string
#                 salaryInt = salaryInt[0:len(salaryInt) - 3] # get rid of the useless parts of the string such that only int's left
#                 if salaryInt[-1] == "C": # some inputs have "CAD" added to the integer so I gotta get rid of that too
#                     continue
#                 salaryInt = int(salaryInt)
#                 totalSalary += salaryInt
#                 countPerson += 1
#         return int(totalSalary / countPerson)

# Enhanced version of the calculateTotalAverageProvince with added readability and better comments.
def calculateTotalAverageProvince(csvFileInput, province):
    # the input is a csv file and the province desired. Province abbreviation is used. ON for ONtario, AB for Alberta etc.
    # check the csv file for the province string format
    # the output is an integer value of the provincial average

    with open(csvFileInput) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row

        total_salary = 0
        count = 0
        numberOfInputs = 0
        numberOfErrorInputs = 0
        for row in csv_reader:
            # Assuming the province name is in the third column (index 2)
            # and the salary is in the fifth column (index 4)

            provinceField = row[2]

            # and then get rid of whatever comes after the comma: split(".")[0]
            if province.upper() in provinceField:
                numberOfInputs += 1
                salaryField = row[4]
                salaryStr = salaryField[1:].replace(",", "").split('.')[
                    0]  # remove the dollar sign [1:] and replace the commas
                try:
                    salary = int(salaryStr)
                    total_salary += salary
                    count += 1
                except ValueError:
                    numberOfErrorInputs += 1
                    print(f"Unable to convert salary '{salaryStr}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return int(total_salary / count) if count > 0 else 0

def getRangeByProvince(csvFileInput, provinceName):

    with open(csvFileInput) as csvFile:
        next(csvFile)
        csv_reader = csv.reader(csvFile, delimiter=",")
        leastValue = math.inf
        greatestValue = 0
        numberOfInputs = 0
        numberOfErrorInputs = 0
        for row in csv_reader:
            provinceField = row[2]
            salaryField = row[4]
            salaryStr = salaryField[1:].replace(",", "").split('.')[0] #remove the dollar sign [1:] and replace the commas
            if (provinceName.upper() in provinceField):
                numberOfInputs += 1
                try:
                    salaryInt = int(salaryStr)
                    if salaryInt > greatestValue:
                        greatestValue = salaryInt
                    if salaryInt < leastValue:
                        leastValue = salaryInt
                except ValueError:
                    numberOfErrorInputs += 1
                    print(f"Unable to convert salary '{salaryStr}' in row: {row}")
    return "Median Range: " + str(leastValue) + " - " + str(greatestValue)


def getMedianCanada(csvFileInput):
    # Calculate the median salary from a CSV file of Canadian SDE incomes.
    # the input is a csv file
    # the output is an integer value of the canadian median
    with open(csvFileInput) as csvFile:
        csv_reader = csv.reader(csvFile)
        headers = next(csv_reader)  # Skip the header row
        salaryArray = []
        numberOfInputs = 0
        numberOfErrorInputs = 0
        for row in csv_reader:
            numberOfInputs += 1
            salaryField = row[4]
            salary_str = salaryField[1:].replace(",", "").split('.')[
                0]  # remove the dollar sign [1:] and replace the commas
            # and then get rid of whatever comes after the comma: split(".")[0]
            salary_str = row[4][1:].replace(",", "").split('.')[0]
            try:
                salary = int(salary_str)
                salaryArray.append(salary)
            except ValueError:
                numberOfErrorInputs += 1
                print(f"Unable to convert salary '{salary_str}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return statistics.median(salaryArray)

def getMedianProvince(csvFileInput, province):


#print("Canada Average", calculateTotalAverageCanada("lastSubSep21.csv")) # check the output for calculateTotalAverageCanada. It appears fine
#print("Ontario Average", calculateTotalAverageProvince("lastSubSep21.csv", "ON")) # check the calculateTotalAverageProvince function. It appears to be workign fine
#print("Ontario Range", getRangeByProvince("lastSubSep21.csv", "ON")) #the format is ass
#print("Canada Median", getMedianCanada("lastSubSep21.csv")) getMedianCanada appears to be working fine
#

# with open("salariesRedditSep23.csv") as csvFile:
#     csv_reader = csv.reader(csvFile, delimiter=",")
#     line_count = 0
#     totalSalary = 0
#     countPerson = 0
#     for row in csv_reader:
#         if ("Ontario" in row[2] and int(row[9][0:1]) >= 0 and int(row[9][0:1]) < 1 ):
#             salaryInt = row[4][1:].replace(",", "")
#             salaryInt = salaryInt[0:len(salaryInt) - 3]
#             salaryInt = int(salaryInt)
#             totalSalary += salaryInt
#             countPerson += 1
#             print(salaryInt)
#             # try:
#             #     if (float(row[9]) <= 1):
#             #         print("tesing")
#             #         #print(row[1], "Salary:" + row[4], row[5], row[6], row[8], "exp:" + row[9], row[10])
#             # except:
#             #     continue
#     print(countPerson)
#     print(totalSalary / countPerson)