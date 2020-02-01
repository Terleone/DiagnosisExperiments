from model.ai import loo_train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read, print_chart

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
    results.append(loo_train_test_iteration(config, samples, use_tree=False))

file = open("My mcc dependency of epochs - breast", "w+")
for i in range(len(epochs)):
    file.write(str(epochs[i]) + ' : ' + str(results[i]) + '\n')
file.close()
