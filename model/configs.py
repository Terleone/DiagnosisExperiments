class AnnConfig:
    silent = False

    def __init__(self, layers, features, epochs, batch_size, data_folder):
        self.layers = layers
        self.features = features
        self.epochs = epochs
        self.batch_size = batch_size
        self.data_folder = data_folder


class TreeConfig:
    def __init__(self, features, data_folder):
        self.features = features
        self.data_folder = data_folder
