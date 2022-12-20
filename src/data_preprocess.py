# Author: 
# Date: 

"""... 
   
Usage: src/data_preprocess.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>           Path of the directory that contains the raw data
--output_path=<output_path>         Path of the output directory for the processed data 

Command to run the script:
python src/data_preprocess.py --input_path='data/raw/UCI_Credit_Card.csv' --output_path='data/processed/'
"""

from docopt import docopt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def create_BP_R(train_df, test_df):
    
    # Create columns in train_df
    train_df['BP_R1'] = train_df['PAY_AMT1']/train_df['BILL_AMT1']
    train_df['BP_R2'] = train_df['PAY_AMT2']/train_df['BILL_AMT2']
    train_df['BP_R3'] = train_df['PAY_AMT3']/train_df['BILL_AMT3']
    train_df['BP_R4'] = train_df['PAY_AMT4']/train_df['BILL_AMT4']
    train_df['BP_R5'] = train_df['PAY_AMT5']/train_df['BILL_AMT5']
    train_df['BP_R6'] = train_df['PAY_AMT6']/train_df['BILL_AMT6']

    # Create columns in test_df
    test_df['BP_R1'] = test_df['PAY_AMT1']/test_df['BILL_AMT1']
    test_df['BP_R2'] = test_df['PAY_AMT2']/test_df['BILL_AMT2']
    test_df['BP_R3'] = test_df['PAY_AMT3']/test_df['BILL_AMT3']
    test_df['BP_R4'] = test_df['PAY_AMT4']/test_df['BILL_AMT4']
    test_df['BP_R5'] = test_df['PAY_AMT5']/test_df['BILL_AMT5']
    test_df['BP_R6'] = test_df['PAY_AMT6']/test_df['BILL_AMT6']

    return train_df, test_df

def create_CB(train_df, test_df):
    
    # Create columns in train_df
    train_df['CB_1'] = train_df['BILL_AMT1']/train_df['LIMIT_BAL']
    train_df['CB_2'] = train_df['BILL_AMT2']/train_df['LIMIT_BAL']
    train_df['CB_3'] = train_df['BILL_AMT3']/train_df['LIMIT_BAL']
    train_df['CB_4'] = train_df['BILL_AMT4']/train_df['LIMIT_BAL']
    train_df['CB_5'] = train_df['BILL_AMT5']/train_df['LIMIT_BAL']
    train_df['CB_6'] = train_df['BILL_AMT6']/train_df['LIMIT_BAL']

    # Create columns in test_df
    test_df['CB_1'] = test_df['BILL_AMT1']/test_df['LIMIT_BAL']
    test_df['CB_2'] = test_df['BILL_AMT2']/test_df['LIMIT_BAL']
    test_df['CB_3'] = test_df['BILL_AMT3']/test_df['LIMIT_BAL']
    test_df['CB_4'] = test_df['BILL_AMT4']/test_df['LIMIT_BAL']
    test_df['CB_5'] = test_df['BILL_AMT5']/test_df['LIMIT_BAL']
    test_df['CB_6'] = test_df['BILL_AMT6']/test_df['LIMIT_BAL']
    
    return train_df, test_df

def replace_inf_nans(train_df, test_df):
    
    # Replace infs and NaNs with 1
    train_df.replace([np.inf, -np.inf, np.nan], 1, inplace=True)
    test_df.replace([np.inf, -np.inf, np.nan], 1, inplace=True)
    
    return train_df, test_df

def save_to_csv(train_df, test_df, output_path):
    
    # Create output file names
    train_output_file = output_path + 'cc_train_df.csv'
    test_output_file = output_path + 'cc_test_df.csv'
    
    # Save to .csv 
    train_df.to_csv(train_output_file)
    test_df.to_csv(test_output_file)
    
def main(input_path, output_path):
    
    # Read raw data from input path as a pandas dataframe
    cc_df = pd.read_csv(input_path)
    
    # Rename 'default.payment.next.month' and 'PAY_0' columns 
    cc_df = cc_df.rename(columns={'default.payment.next.month': 'target', 'PAY_0':'PAY_1'})
    
    # Change levels in 'EDUCATION' column 
    cc_df['EDUCATION'].replace({0: 4, 5: 4, 6: 4}, inplace=True)
    
    # Split data into training and test set (20% test) 
    train_df, test_df = train_test_split(cc_df, test_size=0.2, random_state=123)
    
    # Feature engineering 1: create 'BP_R*' columns (ratio of payment amount to billed amount per month)
    train_df, test_df = create_BP_R(train_df, test_df)
    
    # Feature engineering 2: create 'CB_*' columns (ratio of billed amount to amount of given credit per month)
    train_df, test_df = create_CB(train_df, test_df)
    
    # Replace any infs and NaNs with 1 
    train_df, test_df = replace_inf_nans(train_df, test_df)
    
    # Save processed data as .csv files 
    save_to_csv(train_df, test_df, output_path)

if __name__ == '__main__':
    main(opt['--input_path'], opt['--output_path'])