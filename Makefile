# Author: Shirley Zhang

all : doc/final_report.html doc/final_report.md

# Create preprocessed data files 
data/processed/cc_train_df.csv data/processed/cc_test_df.csv : data/raw/UCI_Credit_Card.csv
	python src/data_preprocess.py --input_path='data/raw/UCI_Credit_Card.csv' --output_path='data/processed/'

# Create tables and figures for EDA 
results/eda/train_target_class_dis.csv results/eda/test_target_class_dis.csv : data/processed/cc_train_df.csv data/processed/cc_test_df.csv
	python src/eda.py --train_df_path='data/processed/cc_train_df.csv' --test_df_path='data/processed/cc_test_df.csv' --output_path='results/eda/'

# Render the final report 
doc/final_report.html : doc/final_report.Rmd results/eda/train_target_class_dis.csv results/eda/test_target_class_dis.csv
	Rscript -e "rmarkdown::render('doc/final_report.Rmd')"

clean : 
	rm -f data/processed/*.csv
	rm -f results/eda/*.csv
	rm -f results/eda/*.png
	rm -f doc/final_report.html
	rm -f doc/final_report.md