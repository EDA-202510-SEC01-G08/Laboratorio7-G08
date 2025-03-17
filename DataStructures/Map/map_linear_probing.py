import map_functions as mf
import map_entry as me
#import array_list as lt

def new_list():
    new_list = {"elements": [],
                "size": 0,
                }
    return new_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def get_element(my_list, index):
    return my_list["elements"][index]

def new_map(num_elements, load_factor, prime=109345121):
    
     capacity = int(mf.next_prime(num_elements/ load_factor))

     x = new_list() #lt.
     dict = {"key": None, "value": None}
     for i in range(capacity):
         add_last(x, dict) #lt.

     map = {"prime": prime, "capacity": capacity, 'scale': 1,
           'shift': 0,'table': x, "current_factor": 0, "limit_factor": load_factor,
             "size": 0} 
    
     return map

def put(my_map, key, value):
     
     hash = mf.hash_value(my_map["table"], key)
     slot = find_slot(my_map, key, hash)

     my_map["table"][slot] = 1


def find_slot(my_map, key, hash_value):
   
   first_avail = None
   found = False
   ocupied = False

   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = get_element(my_map["table"], hash_value) #lt.
            if me.get_key(entry) is None:
               found = True

      elif default_compare(key, get_element(my_map["table"], hash_value)) == 0: #lt.
            first_avail = hash_value
            found = True 
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

     entry = get_element(table, pos)
     if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":#lt.
          result = True
     else:
         result = False
     return result 

def default_compare(key, entry):

     if key == me.get_key(entry):
          return 0
     elif key > me.get_key(entry):
          return 1
     return -1

map = new_map(1,0.5)

print(map)


