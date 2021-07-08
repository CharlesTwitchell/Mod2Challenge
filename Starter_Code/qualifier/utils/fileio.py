# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(modified_loan_list,directory_to_save):
    """takes filtered loan data 
    asks user if they would like to save it
    based on input function offers user opportunity to save file
    """


    header = ["Bank","Credit Score","Debt","Income","Loan Amount","Home Value"]
# Set the output file path
    output_path = Path(directory_to_save)

#creating CSV file using output_path as the file directory.  Then creating a CSV object called cheap_loans
    with open(output_path, 'w', newline='') as csvfile:
        cheap_loans = csv.writer(csvfile)
        #adding header to CSV file
        cheap_loans.writerow(header)
        #looping through the inexpensive_loans list and writing to CSV
        for row in modified_loan_list:
            cheap_loans.writerow(row)
            print(row)
