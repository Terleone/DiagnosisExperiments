from model.ann import train_test_iteration
from model.config import Config
from tools.io_handlers import read

data_folder = 'hepatitis'

hidden_layer_size = -1
features = 19
epochs = 1000
config = Config(hidden_layer_size, features, epochs, data_folder)

samples, names = read(data_folder, file_type='b')
print("Wartość metryki wynosi: {}".format(train_test_iteration(config, samples)))
