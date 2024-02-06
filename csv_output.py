from csv import writer
from scipy import sparse
'''
CSV Output File
-Handles writing data onto csv files
'''

class CSVOutput:
    def __init__(self, path, column_names):
        self.file = open(path, 'w', newline='')
        self.writer = writer(self.file)
        if column_names != None:
            self.writer.writerow(column_names)

    # writes a row onto the csv file
    def process(self, inputs):
        sparsed = sparse.dok_matrix(inputs)
        self.writer.writerow(list(sparsed.keys()))

    def __del__(self):
        self.file.close()
