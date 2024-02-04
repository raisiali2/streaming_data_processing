
#first step extract the csv files from the zip folder
#read each csv file into pandas dataframe
#concatenate these DF into one.
#and finally save the consolidated DF to a new csv file.

import pandas as pd 
import zipfile
import os

#print(pandas.__version__)
directory = '/home/train/datasets/KETI'
dataframe = {}
dataframes_room = {}
columns = ['co2', 'humidity', 'light', 'pir', 'temperature']

