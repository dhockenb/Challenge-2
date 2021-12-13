# @TODO Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by comparing if the customer's debt-to-income is equal to or less than the maximum debt-to-income ratio allowed by the bank
# so that we can assess if the customer will have payment capacity according to the bank's criteria
def filter_debt_to_income(monthly_debt_ratio, bank_list):
    DTI_approval_list = []
    for bank in bank_list:
        if monthly_debt_ratio <= float(bank[3]):
            DTI_approval_list.append(bank)
    return(DTI_approval_list)