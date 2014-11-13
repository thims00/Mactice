#!/usr/bin/env python3.2

############################################################
# Mactice.py - A simple Math Practice application in Python.
# Author: Tomm Smith (root DOT packet AT gmail DOT com)
# Date: 13 NOV 2014
# Version: 0.1
# Notes: In Christ Jesus' name are you forgiven
############################################################




import sys
import getopt


def arith_tbl(func="mul", size=12):
    """ arith_tbl(func="mul", size=12)

    Create an arithmetic table.

    Arguments: @arg str func - The arithmetic function to be applied. One of
                               (add, sub, mul, div)
               @arg int size - How many interations should the table be. 
                               (EG. Up to 12.)

    Return: True upon success, False otherwise. The function will print 
            directly to the terminal on True and return either way.

    Notes: Only supports up to 1000 before the grid is thrown out of symmetry.
    """
    if func == "add":
        prod = "y + x"
    elif func == "sub":
        prod = "y - x"
    elif func == "mul":
        prod = "y * x"
    elif func == "div":
        prod = "y / x"
    else:
        return False

    try:
        int(size)
    except ValueError:
        return False
    
    # Table Header
    print("|-----------------------------------------------------------------------------|")
    print("|     ", end="")
    for i in range(1, size + 1):
        if i < 10:
            print("|  %d  " % i, end="")
        else:
            print("|  %d " % i, end="")

    print("|")
    print("|-----------------------------------------------------------------------------|")
    
    ## Main table body
    # Y plane
    for y in range(1, size + 1):
        if y < 10:
            print("|  %d  " % y, end="")
        else:
            print("|  %d " % y, end="")
    
        # X plane
        for x in range(1, size + 1):
            product=eval(prod)
            if product < 10:
                print("|  %d  " % product, end="")
            elif product < 100:
                print("|  %d " % product, end="")
            elif product < 1000:
                print("| %d " % product, end="")
    
        print("|\n|-----------------------------------------------------------------------------|")




if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "func="])
    print(opts)
    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            print("Help")
        elif opt == "-f" or opt == "--func":
            arith_tbl(arg)



