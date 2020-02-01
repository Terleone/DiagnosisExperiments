from model.ai import loo_train_test_iteration, k_fold_train_test_iteration
from model.configs import TreeConfig
from tools.io_handlers import read

data_folder = 'hepatitis'

samples, names = read(data_folder, file_type='b')
features = len(names)
config = TreeConfig(features, data_folder)
results = k_fold_train_test_iteration(config, samples)

print(results)
