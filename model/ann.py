import keras
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

        model = keras.Sequential([
            keras.layers.Dense(config.features, input_shape=(config.features, )),
            keras.layers.Dense(config.hidden_layer_size, activation='relu'),
            keras.layers.Dense(1, activation='softmax')
        ])
        model.compile(optimizer=keras.optimizers.Adam(),
                      loss='mean_squared_error',
                      metrics=['accuracy'])#=[matthews_corrcoef])
        model.fit(x=train_attributes, y=train_labels, batch_size=len(train_labels), epochs=config.epochs,
                  verbose=1 if not config.silent else 0)

        y_true.append(int(test_labels[0]))
        y_pred.append(int(model.predict(test_attributes).item(0)))
    return matthews_corrcoef(np.asarray(y_true, dtype=int), np.asarray(y_pred, dtype=int))
