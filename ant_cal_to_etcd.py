"""Read the antenna inclinometer calibration data from a YAML file and push it to Etcd.

This is rough-and-ready and needs to be modified to be used for automatic system initialization.
Print statements for debugging should also be removed.
"""

import yaml
import etcd3 as etcd
import json
import time

# Hard-coded Etcd endpoint for use with a tunnel
etcd_endpoint = ['localhost', 2379]

# Hard-coded source appropriate for one particular machine. Interactive entry needs to be removed for system use.
filename = "/dsa_ant_el_cal.yaml"
print(f"\nDefault file name: {filename}")
resp = input("Cal file name (<Enter> for default): ")
if resp != "":
    filename = resp.strip()
stream = open(filename, 'r')

# Read in the YAML file.
cal_table = yaml.load(stream)

# Open the Etcd connection
etcd_client = etcd.client(host=etcd_endpoint[0], port=etcd_endpoint[1])
print(f"Etcd client: {etcd_endpoint[0]}\nPort: {etcd_endpoint[1]}")

# Iterate through the keys for all antennas included in the YAML file, sending them sequentially to Etcd.
for key, val in cal_table.items():
    ant_num = key.replace('ant', '')
    etcd_cal_key = f'/cal/ant/{ant_num}'
    j_pkt = json.dumps({'cal_table': val})
    print(f"Key: {etcd_cal_key},  Val: {j_pkt}")
    etcd_client.put(etcd_cal_key, j_pkt)
    time.sleep(0.25)

etcd_client.close()
