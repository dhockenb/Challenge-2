import questionary
from pathlib import Path
import fire


from utils.fileio import load_csv, save_csv

from utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio
)

from filters.max_loan import filter_max_loan_size
from filters.credit_score import filter_credit_score
from filters.debt_to_income import filter_debt_to_income
from filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    return load_csv(csvpath)

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


def find_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

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

      # Find qualifying loans
   

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )



# Command Line Instruction
# python app.py --credit_score=750 --debt=5000 --income=20000
# python app.py --credit_score=805 --debt=3000 --income=8000

if __name__ == "__main__":
    fire.Fire(run)