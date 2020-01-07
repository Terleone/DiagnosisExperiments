import keras
from keras import backend as K
import numpy as np
from sklearn.metrics import matthews_corrcoef


def train_test_iteration(config, data):
    y_true = []
    y_pred = []

    train_set_size = len(data) - 1
    for sample in data:
        train_samples = [i for i in list(filter(lambda s: s != sample, data))]

        train_attributes = np.empty(shape=(train_set_size, config.features))
        train_labels = np.empty(shape=(train_set_size,))
        for i in range(len(train_samples)):
            _sample = train_samples[i]
            train_attributes[i] = _sample.attributes[0:config.features]
            train_labels[i] = _sample.classification

        sample.attributes = sample.attributes[0:config.features]
        test_attributes = np.empty(shape=(1, config.features))
        test_labels = np.empty(shape=(1,))
        for i in range(len(sample.attributes)):
            test_attributes[0][i] = sample.attributes[i]
        test_labels[0] = sample.classification

        layers = config.layers
        model = keras.Sequential()
        for layer_index in range(len(layers)):
            if layer_index == 0:
                model.add(keras.layers.Dense(layers[layer_index], input_shape=(config.features,)))
            else:
                model.add(keras.layers.Dense(layers[layer_index], activation='relu'))
        model.add(keras.layers.Dense(1, activation='relu'))
        #model.add(keras.layers.Dense(1, activation='softmax')

        """
        model = keras.Sequential([
            keras.layers.Dense(256, input_shape=(config.features, )),
            keras.layers.Dense(192, activation='relu'),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            #keras.layers.Dense(1, activation='softmax')
            keras.layers.Dense(1, activation='relu')
        ])
        """

        model.compile(optimizer=keras.optimizers.Adam(),
                      loss='mean_squared_error',
                      metrics=[matthews_correlation])
        model.fit(x=train_attributes, y=train_labels, batch_size=len(train_attributes), epochs=config.epochs,
                  verbose=1 if not config.silent else 0)

        y_true.append((test_labels[0] - 0.5) * 2)
        y_pred.append((model.predict(test_attributes).item(0) - 0.5) * 2)

    return matthews_corrcoef(np.asarray(y_true, dtype=np.float),
                             np.asarray([-1 if i < 0 else 1 for i in y_pred], dtype=np.float))
                             #np.asarray(y_pred, dtype=np.float))


def matthews_correlation(y_true, y_pred):
    ''' Matthews correlation coefficient
    '''
    y_pred_pos = K.round(K.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos
    y_pos = K.round(K.clip(y_true, 0, 1))
    y_neg = 1 - y_pos
    tp = K.sum(y_pos * y_pred_pos)
    tn = K.sum(y_neg * y_pred_neg)

    fp = K.sum(y_neg * y_pred_pos)
    fn = K.sum(y_pos * y_pred_neg)

    numerator = (tp * tn - fp * fn)
    denominator = K.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return numerator / (denominator + K.epsilon())
