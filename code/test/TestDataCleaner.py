import os
import unittest
import pandas as pd
from IPython.display import display


from manipulate_data.DataCleaner import DataCleaner

def test_data_cleaner():
    train_data_path = "../Thermostability_Prediction/data/raw/train.csv"
    updates_data_path = "../Thermostability_Prediction/data/external/train_updates.csv"

    cleaner = DataCleaner(train_data_path, updates_data_path)
    cleaned_df = cleaner.clean_data()

    display(cleaned_df.describe())
