from xlwt import Workbook
from data_preparing.cleaner import handle_missing_values
from tools.io_handlers import read, write, read_classes

task = 'breast'
flow = 'plain'

samples, names = read(task)
classes = read_classes(task)
c_samples, c_names = handle_missing_values(samples, names, "average", -1, -1)

for c_sample in c_samples:
    if c_sample.classification in [1.0, 2.0]:
        c_sample.classification -= 1
    else:
        raise Exception('Wrong encoding of classes.')

if flow == 'plain':
    c_names_lines = [x + '\n' for x in c_names]
    c_data_lines = [str(int(s.classification)) + ',' + ','.join(s.attributes) + '\n' for s in c_samples]
    write(task, c_names_lines, c_data_lines, 'c')
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
