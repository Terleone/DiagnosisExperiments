from xlwt import Workbook
from data_preparing.cleaner import handle_missing_values
from tools.io_handlers import read, write, read_classes

task = 'hepatitis'
flow = 'plain'

samples, names = read(task)
classes = read_classes(task)
c_samples, c_names = handle_missing_values(samples, names, "average", 5, 5)

if flow == 'plain':
    write(task, 'c')
else:
    wb = Workbook()
    sheet = wb.add_sheet('Sheet 1')
    sheet.write(0, 0, 'Class')
    for i in range(len(c_names)):
        sheet.write(0, i + 1, c_names[i])
    for i in range(len(c_samples)):
        attributes = c_samples[i].attributes
        sheet.write(i + 1, 0, c_samples[i].classification)
        for j in range(len(attributes)):
            sheet.write(i + 1, j + 1, attributes[j])
    wb.save(task + '_prepared.xls')
