#!/usr/bin/python
import sys, getopt, math

def main(argv):
    nb_iteration=0

    def linear_search(array_to_search, value_to_find):
        nonlocal nb_iteration
        is_found = False

        for item in array_to_search:
            nb_iteration+=1
            if item == value_to_find:
                is_found = True
                break
        
        return is_found

    array_to_search = argv[1].split(',')
    value_to_find = argv[2]
    is_found = linear_search(array_to_search, value_to_find)
    print("Number {} {} been found. It took {} tries".format(value_to_find, "has" if is_found else "hasn't" , nb_iteration))

if __name__ == "__main__":
    main(sys.argv)