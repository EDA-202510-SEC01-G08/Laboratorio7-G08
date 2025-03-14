import map_functions as mf
from DataStructures.List import array_list as lt

def new_map(num_elements, load_factor, prime=109345121):
    
    capacity = num_elements/ load_factor
    x = x = lt.new_list()
    dict = {"key": None, "Value": None}
    for i in range(capacity):
         lt.add_last(x, dict) 

    {"prime": prime, "capacity": mf.next_prime(capacity), 'scale': 1,
     'shift': 0,'table': x, "current_factor": 0, "limit_factor": load_factor, "size": 0} #No estoy seguro 