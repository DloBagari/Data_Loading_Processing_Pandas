"""
if data are available on the internet and we need to downloaded to our application with python
using:
urllib
"""
from urllib import request
import pandas as pd
import numpy as np
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


# find the type of data
print(data_frame.dtypes)
# costing data types
data_frame["sepal_length"] = data_frame["sepal_length"].astype(float)
# using masks to do processing on a sub-lines
mask = data_frame["sepal_length"] > 6.0
# type of mask is pandas.core.series.Series
print(mask)
# using mask change the target value to "newValue" where target equal to "iris-virginica"
# fist we need a mask to find where target is equal to "iris-virginica"
mask_target = data_frame["target"] == "virginica"
# apply the mask to dataFrame to change values in target, using .loc[] method
# which is a way to access the data of the matrix with help of row, columns,
# for each value true in mask as row number set column "target" to "new value"
data_frame.loc[mask_target, "target"] = "new Value"
print(data_frame)
# find the values in a columns with no duplication,
print(data_frame["target"].unique())

# group by and find AVG
print(data_frame.groupby(["target"]).mean())

# find variance
print(data_frame.groupby(["target"]).var())

# order by, sorting
print(data_frame.sort_index(by="sepal_length"))

# applying a function on a row or column
# axis = 1 for row, axis = 0 for column
print(data_frame.apply(np.count_nonzero, axis=1).head())
print(data_frame.apply(np.count_nonzero, axis=0).head())

# apply a Function on each element in row or column
# find the length of the string representation of each cell
print(data_frame.applymap(lambda el: len(str(el))))

# select a column to be used as index-column, (primary_key)
data_frame2 = pd.read_csv("a_selection_example_1.csv", index_col=0)
# this dataFrame index start from 100
print(data_frame2)

# access to any cell dataFrame[col][row], this is not matrix: in matrix we do [row][col]
# the [] operator works first on columns and then on the element of the resulting pandas Series
print(data_frame2["val3"][104])

# to have access with something similar ro the access in matrix use .loc[row][col]
print(data_frame2.loc[104]["val3"])

# selecting or accessing by label or index position, mix using .ix[row][col]
print(data_frame2.ix[103]["val2"])
print(data_frame2.ix[103][1])

# using iloc[row, col], where row index is the index of the default dataFrame which starts from zero
print(data_frame2.iloc[1, 2])

# select sub-data
# select col1, col2 with rows from 0 up to 2
print(data_frame2[["val1", "val2"]][0:2])

# is equivalent to previous statement
print(data_frame2.loc[range(100, 102), ["val1", "val2"]])

# is equivalent to previous statement
print(data_frame2.ix[range(100, 102), range(2)])

# is equivalent to previous statement
print(data_frame2.iloc[range(2), range(2)])

