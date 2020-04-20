from model.ai import k_fold_train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read

data_folder = 'hepatitis'

samples, names = read(data_folder, file_type='b')
layers = [256, 192, 128, 64, 64, 64, 64, 64]
features = len(names)
epochs = 1000
batch_size = len(samples) - 1
config = AnnConfig(layers, features, epochs, batch_size, data_folder)
results = k_fold_train_test_iteration(config, samples, False)
print(results)

file = open("ann.txt", "w+")
for i in range(len(results)):
    file.write(str(results[i]) + '\n')
file.close()
