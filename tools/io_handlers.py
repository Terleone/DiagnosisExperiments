from model.sample import Sample
from tools import ml_dir_path

data_file_extension = '.data'
names_file_extension = '.names'


def read(folder):
    names_file = open(ml_dir_path + '\\' + folder + '\\' + folder + names_file_extension, "r")
    names = [x.strip() for x in names_file.readlines()]
    names_file.close()

    data_file = open(ml_dir_path + '\\' + folder + '\\' + folder + data_file_extension, "r")
    sample_lines = data_file.readlines()
    data_file.close()

    samples = []
    for line in sample_lines:
        features = [x.strip() for x in line.split(',')]
        samples.append(Sample(features[0], features[1:]))
    return samples, names


def write_ranked(folder, names_lines, data_lines):
    r_names_file = open(ml_dir_path + '\\' + folder + '\\' + 'r_' + folder + names_file_extension, "w+")
    r_names_file.writelines(names_lines)
    r_names_file.close()

    r_data_file = open(ml_dir_path + '\\' + folder + '\\' + 'r_' + folder + data_file_extension, "w+")
    r_data_file.writelines(data_lines)
    r_data_file.close()
