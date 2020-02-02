from model.ai import loo_train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read

"""Pierwszy dostrajany parametr"""

data_folder = 'hepatitis'
results = []

samples, names = read(data_folder, file_type='b')
layers = [[16, 16, 16],
          [128, 32, 8, 2],
          [256, 128, 64, 32, 16, 8, 4, 2],
          [256, 192, 128, 64, 64, 64, 64, 64]]
features = len(names)
epochs = 100
batch_size = len(samples) - 1
for i in range(len(layers)):
    config = AnnConfig(layers[i], features, epochs, batch_size, data_folder)
    results.append(loo_train_test_iteration(config, samples, use_tree=False))

file = open("My mcc dependency of layers", "w+")
for i in range(len(layers)):
    line = ''
    for layer in layers[i]:
        line = line + str(layer) + ', '
    line = line + ' : ' + str(results[i]) + '\n'
    file.write(line)
file.close()
