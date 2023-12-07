from csv import writer
'''
CSV Output File
-Handles writing data onto csv files
'''

class CSVOutput:
    def __init__(self, path, column_names):
        self.file = open(path, 'w', newline='')
        self.writer = writer(self.file)
        self.writer.writerow(column_names)

    def process(self, inputs):
        self.writer.writerow(inputs)

    def __del__(self):
        self.file.close()
