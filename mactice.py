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
    color = {'BLACK'  : '\033[0;30m',
             'RED'    : '\033[0;31m',
             'cycle'  : ['\033[0;34m', # Blue
                         '\033[0;32m', # Green
                         '\033[0;36m', # Cyan
                         '\033[0;35m', # Purple
                         '\033[0;33m' # Brown
                        ]
            }

    try:
        int(size)
    except ValueError:
        return False
   

    ## Table Header
    print("%s|-----------------------------------------------------------------------------|" % color['BLACK'])
    print("|     |", end="")
    
    # Print 1 through N in the ordered color cycle, Bl, Gr, Cy, Pr, Br, Bl, ...
    for i in range(0, size):
        pos=i % len(color['cycle'])
        print("%s" % color['cycle'][pos], end="")

        hmn_num = i + 1
        if hmn_num < 10:
            print("  %d  " % hmn_num, end="")
        else:
            print("  %d " % hmn_num, end="")
        print("%s|" % color['BLACK'], end="")

    print("%s\n|-----------------------------------------------------------------------------|" %
            color['BLACK'])
    
    ## Main table body
    color_cnt = len(color['cycle'])
    # Y plane
    for y in range(0, size):
        print("%s|" % color['BLACK'], end="")

        clr = color['cycle'][y % color_cnt]
        if y < 9:
            print("  %s%d  %s|" % (clr, y + 1, color['BLACK']), end="")
        else:
            print("  %s%d %s|" % (clr, y + 1, color['BLACK']), end="")

        # X plane
        color_step = 0
        for x in range(0, size):
            # Define our arithmetic operation
            lft = x + 1
            rgt = y + 1
            if func == "add":
                product = lft + rgt
            elif func == "sub":
                product = lft - rgt
            elif func == "mul":
                product = lft * rgt
            elif func == "div":
                product = lft / rgt
            else:
                product = lft * rgt
    
            if x <= y:
                clr = color['cycle'][y  % color_cnt]
            else:
                clr = color['cycle'][x % color_cnt]

            if product < 10:
                print("  %s%d  %s|" % (clr, product, color['BLACK']), end="")
            elif product < 100:
                print("  %s%d %s|" % (clr, product, color['BLACK']), end="")
            elif product < 1000:
                print(" %s%d %s|" % (clr, product, color['BLACK']), end="")

        print("\n|-----------------------------------------------------------------------------|")


def help(msg=None):
    """ help(msg=None)

    Print the [error message and] help information and exit.

    Arguments: @arg str msg - A specific message to display before help output.

    Return: True
    """
    if msg:
        print(msg)

    basename = sys.argv[0].strip('./')

    print("%s - A tool for practicing math on the terminal." % basename)
    print("\t-h,--help - Print this help and exit.")
    print("\t-f,--func [add,sub,mul,div] - Print the math table of provided arithmetic function. Default: times")
    
    return True




if __name__ == "__main__":
    # TODO: Use the getopt error function
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "func="])
    except getopt.GetoptError:
        help("ERROR: You have entered an invalid argument or value.")
        sys.exit(1)
        
    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            help()
        elif opt == "-f" or opt == "--func":
            arith_tbl(arg)
