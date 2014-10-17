# Timer - a quick function to time 
# how long it takes to compute something

import timeit

def time(functionToCall, repititions):
    print "TIMER: "
    setup = "from ellipticcurves import *"
    timer = timeit.Timer(functionToCall, setup)
    print timer.timeit(repititions)
