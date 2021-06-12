#!/usr/bin/python

import sys, getopt, math


def main(argv):
    nbIteration=0

    def binary_search(arrayToSearch, valueToFind, searchRangeBeggining, searchRangeEnd):
        nonlocal nbIteration

        if searchRangeBeggining > searchRangeEnd:
            return False
        

        nbIteration+=1
        midIndex = math.floor((searchRangeBeggining + searchRangeEnd) / 2)

        if valueToFind == arrayToSearch[midIndex]:
            return True
        
        if valueToFind < arrayToSearch[midIndex]:
            return binary_search(arrayToSearch, valueToFind, searchRangeBeggining, midIndex -1)
        else:
            return binary_search(arrayToSearch, valueToFind, midIndex + 1, searchRangeEnd)
    
    print(argv[1].split(','))
    arrayToSearch = argv[1].split(',')
    valueToFind = argv[2]
    isFound = binary_search(arrayToSearch, valueToFind, 0, len(arrayToSearch) -1)
    print("Number {} {} been found. It took {} tries".format(valueToFind, "has" if isFound else "hasn't" , nbIteration))

if __name__ == "__main__":
    main(sys.argv)