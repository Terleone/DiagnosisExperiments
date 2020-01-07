class Config:
    silent = False

    def __init__(self, layers, features, epochs, batch_size, data_folder):
        self.layers = layers
        self.features = features
        self.epochs = epochs
        self.batch_size = batch_size
        self.data_folder = data_folder

"""
    layers = 8
    features = 4
    epochs = 10
    momentum = True

    data_folder = 'hepatitis'
"""

"""
    def __init__(self, parameter, value):
        if parameter == 'hidden_layer_size':
            self.hidden_layer_size = value
        elif parameter == 'features':
            self.features = value
        elif parameter == 'epochs':
            self.epochs = value
        elif parameter == 'momentum':
            self.momentum = value
"""
