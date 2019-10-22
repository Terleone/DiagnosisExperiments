from scipy.stats import stats
from tools.io_handlers import read, write_ranked

folder_name = 'hepatitis'
samples, names = read(folder_name)

ranking = []
for i in range(len(names)):
    die = []
    live = []
    for sample in samples:
        if sample.classification == '1':
            die.append(sample.attributes[i])
        elif sample.classification == '2':
            live.append(sample.attributes[i])
    result = stats.ks_2samp(die, live)
    if result[1] <= 0.1:
        ranking.append((names[i], result[0]))

    print('Wynik dla cechy ' + names[i] + ':\n\t'
        + 'statistics = ' + str(result[0]) + '\n\t'
        + 'pvalue = ' + str(result[1]) + '\n')

ranking.sort(key=lambda tup: tup[1], reverse=True)
print("Cechy wedlug przydatnosci:")
for feature in ranking:
    print("\t" + feature[0])

for sample in samples:
    new_attributes = []
    for r_attr in [x[0] for x in ranking]:
        index = names.index(r_attr)
        attr = sample.attributes[index]
        new_attributes.append(attr)
    sample.attributes = new_attributes

r_names_lines = [x[0] + '\n' for x in ranking]
r_data_lines = [','.join(s.attributes) + '\n' for s in samples]
write_ranked(folder_name, r_names_lines, r_data_lines)
