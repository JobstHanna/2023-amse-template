#! /bin/bash    

echo "start pipeline"
python3 ./data/data_pipeline.py


echo "start testing"
python3 auto_testing.py
#pytest auto_testing.py

echo "end of testing"