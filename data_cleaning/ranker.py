from scipy.stats import stats
from tools.io_handlers import read, write_ranked, read_classes

task = 'hepatitis'
samples, attributes_names = read(task)
classes = read_classes(task)

ranking = []
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
r_data_lines = [','.join(s.attributes) + '\n' for s in samples]
write_ranked(task, r_names_lines, r_data_lines)
