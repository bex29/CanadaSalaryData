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
    # Calculate the median salary from a CSV file of Canadian SDE incomes.
    # the input is a csv file
    # the return value is a string showing the low median and the high median by province
    with open(csvFileInput) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row

        salaryArray = []
        numberOfInputs = 0
        numberOfErrorInputs = 0
        for row in csv_reader:
            provinceField = row[2]
            salaryField = row[4]
            salaryStr = salaryField[1:].replace(",", "").split('.')[
                0]  # remove the dollar sign [1:] and replace the commas
            if (provinceName.upper() in provinceField):
                numberOfInputs += 1
                try:
                    salaryInt = int(salaryStr)
                    salaryArray.append(salaryInt)
                except ValueError:
                    numberOfErrorInputs += 1
                    print(f"Unable to convert salary '{salaryStr}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return statistics.median(salaryArray)

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
                0] # remove the dollar sign [1:] and replace the commas
            try:
                salary = int(salary_str)
                salaryArray.append(salary)
            except ValueError:
                numberOfErrorInputs += 1
                print(f"Unable to convert salary '{salary_str}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return statistics.median(salaryArray)

def getMedianProvince(csvFileInput, provinceName):
    # the input is a csv file and the province desired. Province abbreviation is used. ON for ONtario, AB for Alberta etc.
    # check the csv file for the province string format
    # the output is an integer value of the provincial median pay

    with open(csvFileInput) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row

        salaryArray = []
        numberOfInputs = 0
        numberOfErrorInputs = 0
        for row in csv_reader:
            provinceField = row[2]
            salaryField = row[4]
            salaryStr = salaryField[1:].replace(",", "").split('.')[
                0]  # remove the dollar sign [1:] and replace the commas
            if (provinceName.upper() in provinceField):
                numberOfInputs += 1
                try:
                    salaryInt = int(salaryStr)
                    salaryArray.append(salaryInt)
                except ValueError:
                    numberOfErrorInputs += 1
                    print(f"Unable to convert salary '{salaryStr}' in row: {row}")
        print(f"total number of inputs '{numberOfInputs}'. Number of ignored inputs {numberOfErrorInputs}")
        return statistics.median(salaryArray)


print("Canada Average", calculateTotalAverageCanada("lastSubSep21.csv")) # check the output for calculateTotalAverageCanada. It appears fine
print("Ontario Average", calculateTotalAverageProvince("lastSubSep21.csv", "ON")) # check the calculateTotalAverageProvince function. It appears to be workign fine
print("Ontario Median Range", getRangeByProvince("lastSubSep21.csv", "ON")) #the format is ass
print("Canada Median", getMedianCanada("lastSubSep21.csv")) #getMedianCanada appears to be working fine
print("Ontario Median", getMedianProvince("lastSubSep21.csv", "ON")) #getMedianProvince works as expected
