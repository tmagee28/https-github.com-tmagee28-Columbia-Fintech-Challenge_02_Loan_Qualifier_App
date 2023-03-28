import csv
from pathlib import Path

def save_csv(bank_data_filtered):
    """Creates and saves the loans that the user qualified for to a CSV File."""
    
    #Create headers and a csv path for the qualified loans
    header = ['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']
    bank_data_filtered_csv = Path('bank_data_filtered_csv')

    with open(bank_data_filtered_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer = writer.writerow(header)
        for row in bank_data_filtered:
            writer.writerows(row.values())