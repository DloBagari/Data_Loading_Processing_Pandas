"""
if data are available on the internet and we need to downloaded to our application with python
using:
urllib
"""
from urllib import request
import pandas as pd

# create a request object
requestObject = request.Request("http://aima.cs.berkeley.edu/data/iris.csv")

# get the response object
filePath = request.urlopen(requestObject)
# Read CSV (comma-separated) file into DataFrame
# sep:Delimiter to use, decimal:Character to recognize as decimal point (e.g. use ‘,’ for European data).
# names:List of column names to use. If file contains no header row, then you should explicitly pass header=None
data_frame = pd.read_csv(filePath, sep=",", decimal=",", header=None,
                         names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])

# print first or last rows, default print 5 row, to print 2 rows pass 2 as parameter
print(data_frame.head(), "\n____________________________________________\n")
print(data_frame.tail())

# getting the name of the columns
# data_frame.columns return Index object, to list: list(data_frame.columns
print(data_frame.columns)
print(list(data_frame.columns))

# to extract any column, call data_frame as dictionary
# x is called pandas series no header
X = data_frame["target"]
print(X)

# get multiple columns
# y is called pandas dataFrame it has header
Y = data_frame[["sepal_length", "target"]]
print(Y)

# to find out the size of the data we are dealing with, we call its shape attribute: (rows, columns) tuple
print(data_frame.shape)
print(X.shape)
print(Y.shape)
