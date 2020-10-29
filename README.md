Repo to hold YAML formatted files to be available under the etcd key /cnf/<subsystem>

Filename convention: <subsystem>.yml

Contents:

/cnf/<subsystem>/<number_if_needed>/<other_if_needed>

Example:

/cnf/ant/1/pos:
    # decimal degrees
    lat: 37.1
    lon: 118.1
    elev: 1220.1
/cnf/ant/2/pos:
    lat: 37.2
    lon: 118.2
    elev: 1220.2
/cnf/ant/1/mplimits:
   elevation:
     min: 0.0
     max: 127
   feb_a_temp:
     # Centigrade
     min: -5
     max: 100
     
