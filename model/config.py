class Config:
    hidden_layer_size = 8
    features = 4
    epochs = 10
    momentum = True

    data_folder = 'hepatitis'

    def __init__(self, parameter, value):
        if parameter == 'hidden_layer_size':
            self.hidden_layer_size = value
        elif parameter == 'features':
            self.features = value
        elif parameter == 'epochs':
            self.epochs = value
        elif parameter == 'stratify':
            self.stratify = value
        elif parameter == 'momentum':
            self.momentum = value
