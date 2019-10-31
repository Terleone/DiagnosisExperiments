import keras
import tensorflow


def train_test_iteration(config, data, ann_type):
    for sample in data:
        test_attributes = [].append(sample.attributes)
        test_labels = [].append(sample.classification)
        train_attributes = [i.attributes for i in list(filter(lambda s: s != sample, data))]
        train_labels = [i.classification for i in list(filter(lambda s: s != sample, data))]

        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(config.features,)),
            keras.layers.Dense(config.hidden_layer_size, activation=tensorflow.nn.relu),
            keras.layers.Dense(2, activation=tensorflow.nn.softmax)
        ])
        model.compile(optimizer=keras.optimizers.SGD(lr=0.01, momentum=(1.0 if config.momentum else 0.0),
                                                     decay=0.0, nesterov=False),
                      loss='mean_absolute_error',
                      metrics=['accuracy'])
        model.fit(x=train_attributes, y=train_labels, batch_size=1, epochs=config.epochs,
                  verbose=1)  # if not config.silent else 0)
    model.fit(x=train_attributes, y=train_labels, batch_size=1, epochs=config.epochs,
              verbose=1)  # if not config.silent else 0)
    y_pred = model.predict_classes(test_attributes, 1)
    scores = model.evaluate(test_attributes, test_labels)
    # if not self.silent:
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    return scores[1], test_labels, y_pred
