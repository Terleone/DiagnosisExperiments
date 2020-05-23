from model.ai import loo_train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read

"""Drugi dostrajany parametr"""

data_folder = 'hepatitis'
results = []

samples, names = read(data_folder, file_type='b')
layers = [256, 192, 128, 64, 64, 64, 64, 64]
features = len(names)
epochs = 100
batch_sizes = [float(len(samples) - 1) / 4,
               float(len(samples) - 1) / 2,
               float(len(samples) - 1) * 3 / 4,
               len(samples) - 1]

for i in range(len(batch_sizes)):
    config = AnnConfig(layers, features, epochs, batch_sizes[i], data_folder)
    results.append(loo_train_test_iteration(config, samples, use_tree=False))

file = open("My mcc dependency of step", "w+")
for i in range(len(batch_sizes)):
    file.write(str(batch_sizes[i]) + ' : ' + str(results[i]) + '\n')
file.close()
