"""
read file in chunks using csv package
"""
import csv
import numpy as np

# fist method: DictReader
with open("datasets-uci-iris.csv", "rt") as data_stream:
    # rt mode : read text, same as r
    # DictReader wrap flow of data_stream
    for n, row in enumerate(csv.DictReader(data_stream,
                            fieldnames=["c1", "c2", "c3", "c4", "c5"], dialect="excel")):
        # dialect: just specifies that we are calling the standard comma_separated CSV
        if n == 0:
            print(n, row)
        else:
            break
# second method: reader
with open("datasets-uci-iris.csv", "rt") as data_stream:
    for n, row in enumerate(csv.reader(data_stream, dialect="excel")):
        if n == 0:
            print(row)
        else:
            break


def batch_read(filename, batch=5):
    with open(filename, "rt") as data_stream:
        output = list()
        # iterate over the file
        for n, row in enumerate(csv.reader(data_stream, dialect="excel")):
            if n > 0 and n % batch == 0:
                # yield back the output as numpy array to the main program
                yield (np.array(output))
                # reset output
                output = list()
            output.append(row)
        # iteration is finished yield what is left
        yield (np.array(output))

for chunk in batch_read("datasets-uci-iris.csv", batch=6):
    print(chunk, "\n-----------------------------")
