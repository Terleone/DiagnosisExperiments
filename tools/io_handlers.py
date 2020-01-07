from model.sample import Sample
from tools import ml_dir_path
import matplotlib.pyplot as plt
from os import path

data_file_extension = '.data'
names_file_extension = '.names'
classes_file_extension = '.classes'


def read(task, file_type='f'):
    check_file_type(file_type)
    names_file = open(path.join(ml_dir_path, task, file_type + '_' + task + names_file_extension), "r")
    names = [line.strip() for line in names_file.readlines()]
    names_file.close()

    data_file = open(path.join(ml_dir_path, task, file_type + '_' + task + data_file_extension), "r")
    sample_lines = data_file.readlines()
    data_file.close()

    samples = []
    for line in sample_lines:
        features = [element.strip() for element in line.split(',')]
        samples.append(Sample(float(features[0]), features[1:]))

    if file_type in ['r', 'c', 'b']:
        for i in range(len(samples)):
            attributes = samples[i].attributes
            samples[i].attributes = [float(attr) for attr in attributes]

    return samples, names


def write(task, names_lines, data_lines, file_type):
    check_file_type(file_type)
    names_file = open(path.join(ml_dir_path, task, file_type + '_' + task + names_file_extension), "w+")
    names_file.writelines(names_lines)
    names_file.close()

    data_file = open(path.join(ml_dir_path, task, file_type + '_' + task + data_file_extension), "w+")
    data_file.writelines(data_lines)
    data_file.close()


def read_classes(task):
    classes_file = open(path.join(ml_dir_path, task, task + classes_file_extension), "r")
    lines = classes_file.readlines()
    classes_file.close()
    classes = []
    for elements in [line.strip().split(',') for line in lines]:
        classes.append((elements[0], elements[1]))
    return classes


def check_file_type(file_type):
    if file_type not in ['f', 'c', 'r', 'b']:
        raise Exception('File type is wrong.')


def print_chart(x, y, x_label, y_label, title):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, 'bo')
    ###
    #plt.show()
    ###
    plt.savefig('chart_' + x_label + '&' + y_label + '.png')
    plt.clf()
    plt.close()
