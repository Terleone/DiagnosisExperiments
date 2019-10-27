# The task of this script is to prepare data for statistical analysis in excel
from xlwt import Workbook

from data_cleaning.cleaner import handle_missing_values
from tools.io_handlers import read, read_classes

task = 'hepatitis'
samples, names = read(task)
classes = read_classes(task)

c_samples, c_names = handle_missing_values(samples, names, "average", 5, 5)
wb = Workbook()
sheet = wb.add_sheet('Sheet 1')
for i in range(len(c_names)):
    sheet.write(0, i, c_names[i])
for i in range(len(c_samples)):
    attributes = c_samples[i].attributes
    for j in range(len(attributes)):
        sheet.write(i + 1, j, attributes[j])
wb.save(task + '_prepared.xls')
