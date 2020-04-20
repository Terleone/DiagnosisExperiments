from scipy.stats import wilcoxon

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
