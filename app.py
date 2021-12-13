# import build-in modules/functions

import questionary
from pathlib import Path
import fire
import csv

# import input/out functions from fileio
from utils.fileio import load_csv, save_csv

# import debt to income and loan to value calculators from calculators
from utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio
)

# import filters for loan app
from filters.max_loan import filter_max_loan_size
from filters.credit_score import filter_credit_score
from filters.debt_to_income import filter_debt_to_income
from filters.loan_to_value import filter_loan_to_value

# function for input of banking data from csv file entered on command line
def load_bank_data():

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    return load_csv(csvpath)

# function for input of applicant data from command line
def get_applicant_info():
    credit_score = questionary.text('What is your credit score?').ask()
    debt = questionary.text('What is your monthly debt?').ask()
    income = questionary.text('What is your monthly income?').ask()
    loan_amount = questionary.text('What is the loan amount you are asking for?').ask()
    home_value = questionary.text('What is the home price?').ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return (credit_score, debt, income, loan_amount, home_value)

# function for filtering bank list for qualifying loans
def find_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value):   

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan_amount, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan_amount, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered

    
 # function to save list of qualifying loans using command line input  
def save_qualifying_loans():
        first = questionary.confirm("Do you want to save a list of the qualifying loans?", default=True).ask()
        csvpath = questionary.path("Enter a file path to save as a csv file").ask()
        print(first)
        print(csvpath)
        csvpath = Path(csvpath)
        return csvpath

# the main function for running the script       
def run():
    
    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
    # Ask for csvpath if applicant wants to save list of qualifying loans
    cvpath = save_qualifying_loans()

    # Write csv file of qualifying loans
    writeornot = save_csv(qualifying_loans, cvpath)
    
if __name__ == "__main__":
    fire.Fire(run)