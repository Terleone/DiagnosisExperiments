from model.ann import train_test_iteration
from model.config import Config
from tools.io_handlers import read, print_chart

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
    config = Config(layers, features, epochs, batch_sizes[i], data_folder)
    results.append(train_test_iteration(config, samples))

file = open("My mcc dependency of step - breast", "w+")
for i in range(len(batch_sizes)):
    file.write(str(batch_sizes[i]) + ' : ' + str(results[i]) + '\n')
file.close()
