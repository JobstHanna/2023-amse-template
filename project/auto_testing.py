import pandas as pd
import os.path 

#import sys

#sys.path.append( '/data' )
import data.data_pipeline


def pipeline():
    path = "../data/fine_data.sqlite"

    if os.path.exists(path):
        print("Test result: No defects were dected sucessful")
    else:
        print("Test result: Defects were detected")    


if __name__ == "__main__":
    pipeline()
    #test_cyling_data()
    
#