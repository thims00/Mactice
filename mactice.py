#!/usr/bin/env python3.2

############################################################
# Mactice.py - A simple Math Practice application in Python.
# Author: Tomm Smith (root DOT packet AT gmail DOT com)
# Date: 13 NOV 2014
# Version: 0.1
# Notes: In Christ Jesus' name are you forgiven.
############################################################




import sys
import getopt


def arith_tbl(arith_obj):
    """ arith_tbl(arith_obj)

    Create an arithmetic table.

    Arguments: @arg obj arith_obj - A valid arithmetic object (struct) containing all
                                    the current information.

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


def arith_obj(func, start_pnt, end_pnt, numer=None, denom=None):
    """arith_obj

    A function to create a class (struct) to hold all information pertaining to
    the selected arithmetic function.

    Arguments:

    Return: An object (as described below) of relevant information upon success, 
            False upon other issue internally.

            struct arith_info {
                str function    - The specific arithmetic function to be used. One of, 
                                 add, sub, mul, div.
                str func_char   - The character used to represent the arithmetic function.
                int numerator   - The value of the top number.
                int denominator - The value of the bottom number.
                int start       - An integer of positive value defining where to start.
                int end         - An integer of positive value defining the end point. (<=)
                bool error      - The status of the current arithmetic operation. (Rarely used)
                str msg         - The specific error message pertaining to the toggled error.
            }
    """
    class arinfo:
        function = None
        func_char = None
        numerator = None
        denominator = None
        start = None
        end = None
        error = None
        msg = None

    try:
        int(start_pnt)
        int(end_pnt)
    except ValueError:
        print("ERROR: arith_func(): Second or third argument was a string, integer expected.")
        sys.exit(1)


    if func == 'add':
        arinfo.function = 'add'
        arinfo.func_char = '+'
    elif func == 'sub':
        arinfo.function = 'sub'
        arinfo.func_char = '-'
    elif func == 'mul':
        arinfo.function = 'mul'
        arinfo.func_char = '*'
    elif func == 'div':
        arinfo.function = 'div'
        arinfo.func_char = '/'
    else:
        raise ValueError("arith_func(): First argument was not a valid arithmetic function.")

    if numer:
        arinfo.numerator = numer
    if denom:
        arinfo.denominator = denom

    arinfo.start = start_pnt
    arinfo.end = end_pnt

    return arinfo


def dsply_prob(arith_obj):
    """ dsply_prob(arith_obj)

    Display a math problem in a properly formatted manner.

    Arguments: @arg int top - The top number.
               @arg int bottom - The bottom number.
               @arg str func  - One of add, sub, mul, div

    Return: A string containing the formatted problem upon success, 
            false otherwise. Exceptions are raised internally.
    """
    if not is_arith_obj(arith_obj):
        raise TypeError("dsply_prob(): Provided arithmetic object is not a valid structure.")
    
    output = ""
    top = arith_obj.numerator
    bottom = arith_obj.denominator
    numer_len = len(str(top))
    denom_len = len(str(bottom))
    lrgst_num = None
   
    try:
        int(top)
        int(bottom)
    except ValueError:
        return False

    if numer_len < denom_len:
        lrgst_width = denom_len
        numer_pding = denom_len - numer_len
        denom_pding = 0
    elif numer_len > denom_len:
        lrgst_width = numer_len
        numer_pding = 0
        denom_pding = numer_len - denom_len
    else:
        lrgst_width = numer_len
        numer_pding = 0
        denom_pding = 0
    
    # Display our division differently from our other problems.
    if arith_obj.function == 'div':
        # Pad our first line with space equal to numerator + 1
        for i in range(0, denom_len + 1):
            output += " "
        # finish it with _ 2++ over the denominator length
        for i in range(0, numer_len + 2):
            output += "_"

        output += "\n %d)%d\n" % (arith_obj.denominator, arith_obj.numerator)
        output += "-" * (numer_len + denom_len + 4)

    else:
        # Create our numerator with appropriate padding
        output += "  "
        for i in range(0, numer_pding):
            output += " "
        output += "%d\n" % top
    
        # Arithmetic function character
        # and our denominator with appropriate padding
        output += "%c " % (arith_obj.func_char)
        for i in range(0, denom_pding):
            output += " "
        output += "%d\n" % bottom
    
        # Append a dividing line 1 character longer then 
        # the overall length (including padding.
        for i in range(0, (lrgst_width + 2) + 1):
            output += "-"

    print(output)
    return True


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


def is_arith_obj(arith_obj, validate=False):
    """ is_arith_obj(arith_obj, validate=False)

    Check if provided argument is a valid arith_obj.

    Arguments: @arg obj arith_obj - The object desired to be tested for valid arithmetic object
                                    structure.
               @arg bool validate - Should we validate the integrity of the object's structure?

    Return: True upon existing and being a valid object, false upon other situation.
    """
    if not isinstance(arith_obj, type(arith_obj)):
        return False

    try:
        arith_obj.function
        arith_obj.func_char
        arith_obj.numerator
        arith_obj.denominator
        arith_obj.start
        arith_obj.end
        arith_obj.error
        arith_obj.msg
    except AttributeError:
        return False
    
    if validate:
        if arith_obj.function not in ['add', 'sub', 'mul', 'div']:
            return False

        if arith_obj.func_char not in ['+', '-', '*', '/']:
            return False

        # Test for valid integers
        try:
            int(arith_obj.numerator)
            int(arith_obj.denominator)
            int(arith_obj.start)
            int(arith_obj.end)
        except ValueError:
            return False

        # Test for valid bool value
        if arith_obj.error not in [True, False, None]:
            return False

    return True


def prac_shell(arith_obj):#upto=12, func="mul", rndm=False):
    """ prac_shell(arith_obj) func="mul", rndm=False)

    Practice arithmetic through an interactive shell.

    Argument: @arg obj arith_obj - A valid arithmetic object containing 
                                   required info.

    Return: Object (struct) of results; upon success filled with data, 
            upon failure, False/None.
            EG. Object.status = False
                Object.error = "Some Error Message"
                Object.func = 'mul'
                Object.results = {'2:3' : True, '2:4' : True, '2:5', False, ...}
                ...
    """
    if not is_arith_obj(arith_obj, True):
        raise TypeError("prac_shell(): Supplied arithmetic object is not valid object.")
        
    class results:
        status = False
        func = None
        results = {}
    
    results.func = arith_obj.function

    for step in range(arith_obj.start, arith_obj.end + 1):
        arith_obj.denominator = step
        dsply_prob(arith_obj)
        answer = input(" = ")

        try:
            int(answer)
        except ValueError:
            print("Error, you must enter a numerical number.")
            continue

        prob_str = "%d %s %d" % (arith_obj.numerator, arith_obj.func_char, 
                                 step)

        crct_val = eval(prob_str)

        res_indx = "%d:%d" % (arith_obj.numerator, step)
        if int(answer) != int(crct_val):
            print("Incorrect!")
            print("%s = %d" % (prob_str, crct_val))
            print()

            results.results[res_indx] = False
        else:
            print("Correct!")
            print()

            results.results[res_indx] = True

    return results
         



if __name__ == "__main__":
    # TODO: Use the getopt error function
    try:
        opts, args = getopt.getopt(sys.argv[1:], "dhpf:", ["practice", "help", "func="])
    except getopt.GetoptError:
        help("ERROR: You have entered an invalid argument or value.")
        sys.exit(1)
        
    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            help()
        elif opt == "-f" or opt == "--func":
            if arg:
                arith_tbl(arg)
            else:
                arith_tbl()
        elif opt == "-p" or opt == "--practice":
            res = prac_shell(arith_obj('mul', 1, 5, 1, 5))

        elif opt == "-d":
            print(dsply_prob(arith_obj('add', 1, 12, 29847565432, 82)))
            print(dsply_prob(arith_obj('sub', 1, 12, 29848272298, 82)))
            print(dsply_prob(arith_obj('mul', 1, 12, 29848272298, 82)))
            print(dsply_prob(arith_obj('div', 1, 12, 298, 82)))

    sys.exit(0)
