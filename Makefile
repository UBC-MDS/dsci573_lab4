# Author: Shirley Zhang

all : doc/final_report.md

# Create preprocessed data files 
data/processed/cc_train_df.csv data/processed/cc_test_df.csv : data/raw/UCI_Credit_Card.csv
	python src/data_preprocess.py --input_path="data/raw/UCI_Credit_Card.csv" --output_path="data/processed/"

clean : 
	rm -f data/processed/*.csv