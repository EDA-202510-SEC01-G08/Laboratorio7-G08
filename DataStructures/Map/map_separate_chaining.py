import map_functions as mf
import map_entry as me
from DataStructures.List import array_list as ar
from DataStructures.List import single_linked_list as sl

def new_map(num_elements, load_factor, prime=109345121):
    capacity_prime = mf.next_prime(num_elements/load_factor)
    table = ar.new_list()
    x = sl.new_list()
    for i in range(capacity_prime):
        ar.add_last(table, x)
    my_table = {"prime": 109345121,
                "capacity": capacity_prime,
                "scale": 1,
                "shift": 0,
                "table": table,
                "current_factor": 0,
                "limit_factor": load_factor,
                "size": 0}