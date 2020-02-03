from data_preparing.cleaner import handle_missing_values
from tools.io_handlers import read, write, read_classes

task = 'hepatitis'

samples, names = read(task)
classes = read_classes(task)
c_samples, c_names = handle_missing_values(samples, names, "average", -1, -1)

for c_sample in c_samples:
    if c_sample.classification in [1.0, 2.0]:
        c_sample.classification -= 1
    else:
        raise Exception('Wrong encoding of classes.')

c_names_lines = [x + '\n' for x in c_names]
c_data_lines = [str(int(s.classification)) + ',' + ','.join(s.attributes) + '\n' for s in c_samples]
write(task, c_names_lines, c_data_lines, 'c')
