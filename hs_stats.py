from math import *
from collections import Counter
import numpy as np

def mean(data) :
    return fsum(data)/len(data)

def median(data) :
    i, j = 0, len(data)-1

    if len(data)%2 == 0 :
        while i != j-1 :
            i += 1
            j -= 1
        return (data[i]+data[j])/2

    else :
        while i != j :
            i += 1
            j -= 1
        return data[i]
    
def mode(data) :
    hashtable = dict(Counter(data).most_common())
    
    modes = set()
    val = -1

    for x,freq in hashtable.items() :
        if freq > val :
            modes = {x}
            val = freq
        if freq == val :
            modes.add(x)
    
    return modes

# population variance
def p_variance(data) :
    m = mean(data)
    sum = fsum([(x - m)**2 for x in data])
    return sum/len(data)

# sample variance
def s_variance(data) :
    m = mean(data)
    sum = fsum([(x - m)**2 for x in data])
    return sum/(len(data)-1)

def standard_deviation(data, var = True) :
    # var : true -> sample variance / false -> population variance
    if var : return sqrt(s_variance(data))
    return sqrt(p_variance(data))

def z_score(data,x) :
    return (x-mean(data))/standard_deviation(data)