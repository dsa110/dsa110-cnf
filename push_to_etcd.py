import json
import yaml
import dsautils.dsa_store as ds
import sys

# open etcd connection
my_ds = ds.DsaStore()

# first argument is key, second argument is file
key = sys.argv[1]
if len(sys.argv) == 3:
    print(f"Pushing {sys.argv[2]} to {key}...")
    fl = sys.argv[2]

    # read file
    with open(fl, 'r') as stream:
        try:
            dct = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print('cannot open yaml file')
            exit(1)

    # push to etcd
    my_ds.put_dict(key, dct)

else:
    print(f"No file provided. Printing {key} values...")
    dct = my_ds.get_dict(key)
    print(dct)





