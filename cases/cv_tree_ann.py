from model.ai import stratified_kfold_split, cv
from model.configs import TreeConfig, AnnConfig
from tools.io_handlers import read

data_folder = 'hepatitis'

for i in range(10):
    samples, names = read(data_folder, file_type='b')
    features = len(names)
    packs = stratified_kfold_split(features, samples)

    config = TreeConfig(features, data_folder)
    results = cv(config, packs)

    file = open("tree.txt", "a+")
    for j in range(len(results)):
        file.write(str(results[j]) + '\n')
    file.close()

    samples, names = read(data_folder, file_type='b')
    layers = [256, 192, 128, 64, 64, 64, 64, 64]
    features = len(names)
    epochs = 1000
    batch_size = len(samples) - 1
    config = AnnConfig(layers, features, epochs, batch_size, data_folder)
    results = cv(config, packs, False)

    file = open("ann.txt", "a+")
    for j in range(len(results)):
        file.write(str(results[j]) + '\n')
    file.close()
