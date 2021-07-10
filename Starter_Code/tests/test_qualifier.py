# Import pathlib
from Starter_Code.app import find_qualifying_loans
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

#testing function to check if save function DOES save to a CSV file
def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    assert qualifier.utils.fileio.save_csv([1,2,3],"C:\Users\Chuckles\Desktop\BootCampChallengesRoughlVersion\Mod2Challenge\Starter_Code\data\output.qualifying_loans.csv") == "C:\Users\Chuckles\Desktop\BootCampChallengesRoughlVersion\Mod2Challenge\Starter_Code\data\output.qualifying_loans.csv"

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!

    #If working prooperly, find_qualifying_loans should return 6 lenders for the above info
    #Setting test to determine if the number of lenders is 6

    assert len(find_qualifying_loans(bank_data,current_credit_score,debt,income,loan,home_value)) == 6