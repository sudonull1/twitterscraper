#!/usr/bin/env python3
import os
import glob
import pandas as pd
os.chdir("/home/alok/twitterwork/models/tweets")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for files in all_filenames:
    print(files)


combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "Q1_2020_F.csv", index=False, encoding='utf-8-sig')
