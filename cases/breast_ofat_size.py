from model.ai import train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read, print_chart

"""Pierwszy dostrajany parametr"""

data_folder = 'breast'
results = []

samples, names = read(data_folder, file_type='b')
layers = [[16, 16, 16],
          [128, 32, 8, 2]]
'''
          [256, 128, 64, 32, 16, 8, 4, 2],
          [256, 192, 128, 64, 64, 64, 64, 64],
          [256, 256, 192, 192, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2],
          [64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64],
          [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]]'''
features = len(names)
epochs = 1000
batch_size = len(samples) - 1
for i in range(len(layers)):
    config = AnnConfig(layers[i], features, epochs, batch_size, data_folder)
    results.append(train_test_iteration(config, samples, use_tree=False))

file = open("My mcc dependency of layers - breast", "w+")
for i in range(len(layers)):
    line = ''
    for layer in layers[i]:
        line = line + str(layer) + ', '
    line = line + ' : ' + str(results[i]) + '\n'
    file.write(line)
file.close()
