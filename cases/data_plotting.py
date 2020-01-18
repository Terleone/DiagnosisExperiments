from tools.io_handlers import read
import matplotlib.pyplot as plt

samples, names = read('breast', file_type='c')
for n in range(len(names)):
    plt.title('Wpływ atrybutu ' + names[n] + ' na klasyfikację')
    plt.xlabel(names[n])
    plt.ylabel('Klasa')
    plt.plot([s.attributes[n] for s in samples], [s.classification + 1 for s in samples], 'bo')
    plt.savefig(names[n] + '.png')
    plt.clf()
    plt.close()
