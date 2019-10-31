from scipy.stats import stats
from tools.io_handlers import read, write, read_classes

task = 'hepatitis'
samples, attributes_names = read(task, 'c')
classes = read_classes(task)

ranking = []

print(samples)

for i in range(len(attributes_names)):
    population_per_class = {class_id: [] for class_name, class_id in classes}

    for sample in samples:
        population_per_class[sample.classification].append(sample.attributes[i])

    if len(population_per_class) != 2:
        raise Exception('Solution anticipated two classes. Got {}'.format(len(population_per_class)))
    populations = [population for population in population_per_class.values()]
    result = stats.ks_2samp(populations[0], populations[1])

    if result[1] <= 0.1:
        ranking.append((attributes_names[i], result[0]))

    print('Wynik dla cechy ' + attributes_names[i] + ':\n\t'
          + 'statistics = ' + str(result[0]) + '\n\t'
          + 'pvalue = ' + str(result[1]) + '\n')

ranking.sort(key=lambda tup: tup[1], reverse=True)
print("Cechy wedlug przydatnosci:")
for feature in ranking:
    print("\t" + feature[0])

for sample in samples:
    new_attributes = []
    for r_attr in [x[0] for x in ranking]:
        index = attributes_names.index(r_attr)
        attr = sample.attributes[index]
        new_attributes.append(attr)
    sample.attributes = new_attributes

r_names_lines = [x[0] + '\n' for x in ranking]
r_data_lines = [s.classification + ',' + ','.join(s.attributes) + '\n' for s in samples]
write(task, r_names_lines, r_data_lines, 'r')

# Script that finds empty values
"""
r_samples, r_names = read(task, ranked=True)
print('\nThere is: ' + str(len(r_samples)) + ' samples.\n')
for sample in r_samples:
    empty_values = 0
    for attr in sample.attributes:
        if attr == '?':
            empty_values = empty_values + 1
    print('Sample nr: ' + str(r_samples.index(sample)) + ' contains ' + str(empty_values) + ' empty values.')

not_full_samples = 0
for sample in r_samples:
    if len(list(filter(lambda x: x == '?', sample.attributes))) != 0:
        not_full_samples = not_full_samples + 1
print('\nThere is ' + str(not_full_samples) + ' that have empty values.\n')

not_full_samples_without_protime = 0
for sample in r_samples:
    if len(list(filter(lambda x: x == '?' and x.index != r_names.index('PROTIME'), sample.attributes))) != 0:
        not_full_samples_without_protime = not_full_samples_without_protime + 1
print('\nThere is ' + str(not_full_samples_without_protime) + ' that have empty values (protime not included).\n')

for name in r_names:
    empty_values = 0
    for sample in r_samples:
        if sample.attributes[r_names.index(name)] == '?':
            empty_values = empty_values + 1
    print('Attribute: ' + name + ' contains ' + str(empty_values) + ' empty values.')
"""
