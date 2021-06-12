#!/usr/bin/python

import sys, getopt, math

def main(argv):
    nb_iteration=0

    def binary_search(array_to_search, value_to_find, search_range_beggining, search_range_end):
        nonlocal nb_iteration

        if search_range_beggining > search_range_end:
            return False
        

        nb_iteration+=1
        mid_index = math.floor((search_range_beggining + search_range_end) / 2)

        if value_to_find == array_to_search[mid_index]:
            return True
        
        if value_to_find < array_to_search[mid_index]:
            return binary_search(array_to_search, value_to_find, search_range_beggining, mid_index -1)
        else:
            return binary_search(array_to_search, value_to_find, mid_index + 1, search_range_end)
    
    print(argv[1].split(','))
    array_to_search = argv[1].split(',')
    value_to_find = argv[2]
    is_found = binary_search(array_to_search, value_to_find, 0, len(array_to_search) -1)
    print("Number {} {} been found. It took {} tries".format(value_to_find, "has" if is_found else "hasn't" , nb_iteration))

if __name__ == "__main__":
    main(sys.argv)