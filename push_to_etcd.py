import json
import yaml
import dsautils.dsa_store as ds
import sys

# first argument is key, second argument is file
key = sys.argv[1]
fl = sys.argv[2]

# read file
with open(fl, 'r') as stream:
    try:
        dct = yaml.load(stream)
    except yaml.YAMLError as exc:
        print('cannot open yaml file')
        exit(1)

# open etcd connection
my_ds = ds.DsaStore()

# push to etcd
my_ds.put_dict(key,dct)


