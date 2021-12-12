
# This function loads a CSV file from the filepath defined in `csvpath`
import csv
def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# This function writes a CSV file from 'find_qualifying_loans'
def save_csv(csvpath, find_qualifying_loans, header=None):
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        if header:
             csvwriter.writerow(header)
        for row in find_qualifying_loans:
            csvwriter.writerow(row.values())

     
