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
    return my_table

def put(my_table, key, value):
    hash = mf.hash_value(my_table,key)
    if sl.is_present(my_table["table"][hash], key, default_compare) != -1:
        pos = sl.is_present(my_table["table"][hash], key, default_compare)
        sl.change_info(my_table["table"][hash], pos, {"key": key, "value": value})
    elif sl.is_present(my_table["table"][hash], key, default_compare) == -1:
        sl.add_last(my_table["table"][hash], me.new_map_entry(key, value))
        #Faltaría añadir un elemento a la lista y hacer el rehash en caso de que el current factor supere al load factor
    return my_table

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    elif key < me.get_key(entry):
        return -1

def contains(my_table, key):
    in_table = False
    hash = mf.hash_value(my_table, key)
    if sl.is_present(my_table["table"][hash], key, default_compare) != -1:
        in_table = True
    return in_table

def remove(my_table, key):
    hash = mf.hash_value(my_table, key)
    pos = sl.is_present(my_table["table"][hash],key, default_compare)
    sl.delete_element(my_table["table"][hash], pos)
    return my_table

def get(my_table, key):
    hash = mf.hash_value(my_table, key)
    pos = sl.is_present(my_table["table"][hash],key, default_compare)
    info = sl.get_element(my_table["table"][hash], pos)
    value = me.get_value(info)
    return value

def size(my_table):
    size = my_table["size"]
    return size

def is_empty(my_table):
    empty = False
    if size(my_table) == 0:
        empty = True
    return empty

def key_set(my_table):
    pos = 0
    lista_llaves = ar.new_list()
    while pos < my_table["size"]:
        slot_size = sl.size(my_table["table"][pos])
        for i in range(slot_size):
            llave = me.get_key(sl.get_element(my_table["table"][pos],i))
            ar.add_last(lista_llaves, llave)
        pos += 1
    return lista_llaves

def value_set(my_table):
    pos = 0
    lista_valores = ar.new_list()
    while pos < my_table["size"]:
        slot_size = sl.size(my_table["table"][pos])
        for i in range(slot_size):
            valor = me.get_value(sl.get_element(my_table["table"][pos],i))
            ar.add_last(lista_valores, valor)
        pos += 1
    return lista_valores

def rehash(my_table):
    #TODO: Completar la función rehash
    pass