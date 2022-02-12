import json
import yaml
import dsautils.dsa_store as ds
import sys
import numpy as np
import time

# first argument is file name
fl = sys.argv[1]

# read file
with open(fl, 'r') as stream:
    try:
        dct = yaml.load(stream)
    except yaml.YAMLError as exc:
        print('cannot open yaml file')
        exit(1)

# open etcd connection
my_ds = ds.DsaStore()

# assumes 117 antennas
for ant in np.arange(1,118):
    try:
        arr = dct['ant'+str(ant)]
        dd = {'cal_table': arr}
        print(ant,dd)
        my_ds.put_dict('/cal/ant/'+str(ant),dd)
        time.sleep(0.1)
    except:
        print('no antenna',ant)
    

    

