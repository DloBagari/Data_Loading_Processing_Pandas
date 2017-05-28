"""
if CSV file contains a header and some missing data for some columns, pandas automatically gave the columns their
actual name after pick them from the first row . if we do not pass parameters to define the type of columns
columns will be prased as integer or string.
"""

import pandas as pd
data_frame = pd.read_csv("a_loading_example_1.csv", sep=",", decimal=".")
# date will be printed as integer
print(data_frame.head())

data_frame = pd.read_csv("a_loading_example_1.csv", sep=",", decimal=",", parse_dates=[0])
print(data_frame)
# replace missing values NaN with something else: int or string
print(data_frame.fillna("empty"))

# file contain bad line read_csv will stop and raise exception
# to read only good lines and skip bad lines use parameter error_bad_lines=False

# reading file contains bad lines, bad lines will be skipped
data_frame2 = pd.read_csv("a_loading_example_2.csv", sep=",", parse_dates=[0], error_bad_lines=False)
print(data_frame2)

# reading data as chunks when data does not fit into memory
# read_csv does not return dataFrame object it returns an iterator_object

data_chunk = pd.read_csv("datasets-uci-iris.csv", sep=",", header=None,
                         names=["C1", "c2", "c3", "c4", "c5"], chunksize=10)
# to read data we iterate over it
for chunk in data_chunk:
    print("Shape: ", chunk.shape)
    print(chunk, "\n")

# other method to read data in chunk is to ask for iterator
data_iterator = pd.read_csv("datasets-uci-iris.csv", sep=",", header=None,
                            names=["C1", "c2", "c3", "c4", "c5"], iterator=True)
# get a chunk of 10 lines, return a dataFrame set contains 10 lines
print(data_iterator.get_chunk(10))
print(data_iterator.get_chunk(30))
print(data_iterator.get_chunk(10).shape)