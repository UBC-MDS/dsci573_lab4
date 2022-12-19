# Author: 
# Date: 

"""... 
   
Usage: src/eda.py --train_df_path=<train_df_path> --test_df_path=<test_df_path> --output_path=<output_path>

Options:
--train_df_path=<train_df_path>     Path of the directory that contains ...
--test_df_path=<test_df_path>       Path of the directory that contains ...
--output_path=<output_path>         Path of the output directory for ...

Command to run the script:
python src/eda.py --train_df_path='data/processed/cc_train_df.csv' --test_df_path='data/processed/cc_test_df.csv' --output_path='results/eda/'
"""

from docopt import docopt
import pandas as pd
import altair as alt 
import vl_convert as vlc
alt.data_transformers.enable('data_server')

opt = docopt(__doc__)
   
def class_dis_table(data_df):
    
    # Create a dataframe with count and percent columns 
    target_class_dis = pd.DataFrame({'class': [0, 1]})
    target_class_dis.index.name = 'class'
    target_class_dis['count'] = data_df['target'].value_counts()
    target_class_dis['percent'] = data_df['target'].value_counts(normalize=True)
    target_class_dis['percent'] = round(target_class_dis['percent'] * 100, 1)
    target_class_dis = target_class_dis.set_index('class')
    
    return target_class_dis

def save_to_csv(df, output_path, file_name):
    
    # Create output file name
    output_file_path = output_path + file_name
    
    # Save to .csv 
    df.to_csv(output_file_path)
    
def column_dis_histogram(df, chart_title):
    
    # Create histograms for all columns, coloured by target class
    repeated_histogram = alt.Chart(df, width=200, height=100).mark_bar().encode(
        x=alt.X(alt.repeat(), bin=alt.Bin(maxbins=70)),
        y='count()',
        color='target'
    ).repeat(
        df.select_dtypes('number').nunique().to_frame('count').index.tolist(),
        columns=3
    ).properties(
        title=chart_title
    )
    
    return repeated_histogram
    
def save_chart(chart, filename, scale_factor=1):
    '''
    Save an Altair chart using vl-convert
    
    Parameters
    ----------
    chart : altair.Chart
        Altair chart to save
    filename : str
        The path to save the chart to
    scale_factor: int or float
        The factor to scale the image resolution by.
        E.g. A value of `2` means two times the default resolution.
    '''
    if filename.split('.')[-1] == 'svg':
        with open(filename, "w") as f:
            f.write(vlc.vegalite_to_svg(chart.to_dict()))
    elif filename.split('.')[-1] == 'png':
        with open(filename, "wb") as f:
            f.write(vlc.vegalite_to_png(chart.to_dict(), scale=scale_factor))
    else:
        raise ValueError("Only svg and png formats are supported") 
    
def main(train_df_path, test_df_path, output_path):
    
    # Read processed training and test data from input path as pandas dataframes
    train_df = pd.read_csv(train_df_path)
    test_df = pd.read_csv(test_df_path)
    
    # Create a target class distribution table for the training data and save to a .csv file 
    train_target_class_dis_df = class_dis_table(train_df)
    save_to_csv(train_target_class_dis_df, output_path, 'train_target_class_dis.csv')
    
    # Create a target class distribution table for the test data and save to a .csv file 
    test_target_class_dis_df = class_dis_table(test_df)
    save_to_csv(test_target_class_dis_df, output_path, 'test_target_class_dis.csv') 
    
    # Create a histogram of distributions of all columns/features
    chart_title = 'Histogram of Distribution of Values for Each Feature'
    repeated_histogram = column_dis_histogram(train_df, chart_title)
    
    # Save histogram as .png 
    #filename = output_path + 'feature_dis_histogram.png'
    #save_chart(repeated_histogram, filename, scale_factor=1)
    
    ##### test save .png 
    test = alt.Chart(train_df[['ID', 'target']], width=200, height=100).mark_bar().encode(
        x=alt.X('ID', bin=alt.Bin(maxbins=70)),
        y='count()',
        color='target'
    )
    filename = output_path + 'test.png'
    test
    #save_chart(test, filename, scale_factor=1)
    

if __name__ == '__main__':
    main(opt['--train_df_path'], opt['--test_df_path'], opt['--output_path'])