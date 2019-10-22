import os

cur_dir = os.path.curdir
os.chdir(os.path.pardir)
local_config_file = open('local_config.md')
ml_dir_path = str.strip(local_config_file.readline())
local_config_file.close()
os.chdir(cur_dir)
