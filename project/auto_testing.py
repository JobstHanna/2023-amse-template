import pandas as pd
import os.path 
#import sys

#sys.path.append( '/data' )
import data.data_pipeline


def pipeline():
    data.data_pipeline.gather_data()

    if os.path.exists("./data/my_data.sqlite"):
        print("Test result: No defects were dected sucessful")
    else:
        print("Test result: Defects were detected")    


if __name__ == "__main__":
    pipeline()
    #test_cyling_data()