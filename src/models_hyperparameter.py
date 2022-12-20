# Author: 
# Date: 

"""... 
   
Usage: src/models_hyperparameters.py --input_path=<input_path> --output_path=<output_path>

Options:
--input_path=<input_path>           Path of the directory that contains ...
--output_path=<output_path>         Path of the output directory for ...

Command to run the script:
python src/models_hyperparameters.py --input_path="..." --output_path="..."
"""


from docopt import docopt
import pandas as pd

opt = docopt(__doc__)


def main(input_path, output_path):
    
    
if __name__ == "__main__":
    main(opt["--input_path"], opt["--output_path"])