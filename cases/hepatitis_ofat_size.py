from model.ann import train_test_iteration
from model.config import Config
from tools.io_handlers import read, print_chart

data_folder = 'hepatitis'

hidden_layer_sizes = [2, 3, 5, 8, 13, 21, 34]
features = 15
epochs = 10

results = []
samples, names = read(data_folder, file_type='c')
for hidden_layer_size in hidden_layer_sizes:
    config = Config(hidden_layer_size, features, epochs, data_folder)
    results.append(train_test_iteration(config, samples))
print_chart(hidden_layer_sizes, results, 'Rozmiar warstwy ukrytej', 'Accuracy',
            'Zależnośc między rozmiarem warstwy ukrytej a wartością metryki accuracy')
