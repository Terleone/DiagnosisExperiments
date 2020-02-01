import xlwt
from xlwt import Workbook
from scipy.stats import wilcoxon
from model.ai import train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read, print_chart

"""Pierwszy dostrajany parametr"""

data_folder = task = 'breast'
results = []

samples, names = read(data_folder, file_type='b')
layers = [[16, 16, 16],
          [128, 32, 8, 2],
          [256, 128, 64, 32, 16, 8, 4, 2],
          [256, 192, 128, 64, 64, 64, 64, 64],
          [256, 256, 192, 192, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2],
          [64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64],
          [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]]
features = len(names)
epochs = 1000
batch_size = len(samples) - 1
for i in range(len(layers)):
    config = AnnConfig(layers[i], features, epochs, batch_size, data_folder)
    results.append(train_test_iteration(config, samples, False, True))

style_red = xlwt.easyxf('pattern: pattern solid, fore_colour red;')
style_green = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
style_black = xlwt.easyxf('pattern: pattern solid, fore_colour black;')
wb = Workbook()
sheet1 = wb.add_sheet('Sizes')
sheet1.write(0, 0, 'ANN')
for i in range(len(layers)):
    sheet1.write(i + 1, 0, 'Sieć nr ' + str(i + 1))
    sheet1.write(0, i + 1, 'Sieć nr ' + str(i + 1))
for i in range(len(layers)):
    for j in range(len(layers)):
        if i == j or results[i] == results[j]:
            sheet1.write(i + 1, j + 1, str(1), style_black)
        else:
            p_value = wilcoxon(results[i], results[j])[1]
            sheet1.write(i + 1, j + 1, str(p_value), style_green if p_value <= 0.05 else style_red)

"""Drugi dostrajany parametr"""

data_folder = 'breast'
results = []

samples, names = read(data_folder, file_type='b')
layers = [16, 16, 16]
features = len(names)
epochs = 1000
batch_sizes = [float(len(samples) - 1) / 4,
               float(len(samples) - 1) / 2,
               float(len(samples) - 1) * 3 / 4,
               len(samples) - 1]

for i in range(len(batch_sizes)):
    config = AnnConfig(layers, features, epochs, batch_sizes[i], data_folder)
    results.append(train_test_iteration(config, samples, False, True))

sheet2 = wb.add_sheet('Steps')
sheet2.write(0, 0, 'Step')
for i in range(len(batch_sizes)):
    sheet2.write(i + 1, 0, str(int(batch_sizes[i])))
    sheet2.write(0, i + 1, str(int(batch_sizes[i])))
for i in range(len(batch_sizes)):
    for j in range(len(batch_sizes)):
        if i == j or results[i] == results[j]:
            sheet2.write(i + 1, j + 1, str(1), style_black)
        else:
            p_value = wilcoxon(results[i], results[j])[1]
            sheet2.write(i + 1, j + 1, str(p_value), style_green if p_value <= 0.05 else style_red)

"""Trzeci dostrajany parametr"""

data_folder = 'breast'
results = []

samples, names = read(data_folder, file_type='b')
layers = [16, 16, 16]
features = len(names)
epochs = [10, 50, 100, 500, 750, 1000, 2500, 5000, 7500, 10000]
batch_size = float(len(samples) - 1) / 2

for i in range(len(epochs)):
    config = AnnConfig(layers, features, epochs[i], batch_size, data_folder)
    results.append(train_test_iteration(config, samples, False, True))

sheet3 = wb.add_sheet('Epochs')
sheet3.write(0, 0, 'Epoch')
for i in range(len(batch_sizes)):
    sheet3.write(i + 1, 0, str(epochs[i]))
    sheet3.write(0, i + 1, str(epochs[i]))
for i in range(len(epochs)):
    for j in range(len(epochs)):
        if i == j or results[i] == results[j]:
            sheet3.write(i + 1, j + 1, str(1), style_black)
        else:
            p_value = wilcoxon(results[i], results[j])[1]
            sheet3.write(i + 1, j + 1, str(p_value), style_green if p_value <= 0.05 else style_red)
wb.save('wilcoxon.xls')
