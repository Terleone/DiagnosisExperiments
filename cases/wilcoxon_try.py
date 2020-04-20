import xlwt
from xlwt import Workbook
from scipy.stats import wilcoxon
from model.ai import loo_train_test_iteration
from model.configs import AnnConfig
from tools.io_handlers import read, print_chart

tree_file = open('tree.txt', 'r')
tree_lines = tree_file.readlines()
tree_data = [float(x) for x in tree_lines]
tree_file.close()

ann_file = open('ann.txt', 'r')
ann_lines = ann_file.readlines()
ann_data = [float(x) for x in ann_lines]
ann_file.close()

results = wilcoxon(tree_data, ann_data)
print(results)
