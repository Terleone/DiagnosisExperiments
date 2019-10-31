def handle_missing_values(samples, names, method, sample_tolerance, feature_tolerance):
    if sample_tolerance >= 0:
        samples = filter_samples(samples, sample_tolerance)

    if feature_tolerance >= 0:
        filter_features(samples, names, feature_tolerance)

    fill_missing_data(samples, method)
    return samples, names


def filter_samples(samples, sample_tolerance):
    return list(filter(lambda s:
                       len(list(filter(lambda a: a == '?', s.attributes))) <= sample_tolerance,
                       samples))


def filter_features(samples, names, feature_tolerance):
    features_to_remove = []
    for name in names:
        empty_values = 0
        for sample in samples:
            if sample.attributes[names.index(name)] == '?':
                empty_values = empty_values + 1
        if empty_values > feature_tolerance:
            features_to_remove.append(names.index(name))
    features_to_remove.reverse()
    for i in range(len(samples)):
        for attr_ind in features_to_remove:
            samples[i].attributes.pop(attr_ind)
    for attr_ind in features_to_remove:
        names.pop(attr_ind)


def fill_missing_data(samples, method):
    features = len(samples[0].attributes)
    if method == 'average':
        averages = []
        for i in range(0, features):
            partial_sum = 0.0
            for sample in samples:
                feature = sample.attributes[i]
                if feature != '?':
                    partial_sum = partial_sum + float(feature)
            averages.append(partial_sum / len(samples))
        for sample in samples:
            for i in range(0, features):
                if sample.attributes[i] == '?':
                    sample.attributes[i] = str(averages[i])
    elif method == 'median':
        medians = []
        for i in range(0, features):
            values = [sample.attributes[i] for sample in samples]
            values.sort()
            length = len(values)
            medians.append(values[int(length / 2)] if length % 2 == 0
                           else float(values[int(length / 2)]) + float(values[int((length / 2)) - 1]))
        for sample in samples:
            for i in range(0, features):
                if sample.attributes[i] == '?':
                    sample.attributes[i] = str(medians[i])
