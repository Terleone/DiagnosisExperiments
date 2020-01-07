from model.ann import train_test_iteration
from model.config import Config
from tools.io_handlers import read, print_chart

data_folder = 'hepatitis'

layers = [256, 192, 128, 64, 64, 64, 64, 64]
#epochs = [10, 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 4500, 5000, 7500, 10000]
epochs = [10, 100, 500, 1000]


results = []
samples, names = read(data_folder, file_type='b')
for e in epochs:
    config = Config(layers, len(names), e, len(samples) - 1, data_folder)
    results.append(train_test_iteration(config, samples))

print_chart(epochs, results, 'Liczba epok', 'Wartość metryki MCC',
            'Zależnośc między liczbą epok a wartością metryki MCC')
