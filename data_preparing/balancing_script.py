from data_preparing.cleaner import balance_data, normalize_data
from tools.io_handlers import read, write

task = 'hepatitis'

samples, names = read(task, 'c')

balance_data(samples)
normalize_data(samples)

b_names_lines = [x + '\n' for x in names]
b_data_lines = [str(int(s.classification)) + ',' + ','.join([str(a) for a in s.attributes]) + '\n' for s in samples]
write(task, b_names_lines, b_data_lines, 'b')
