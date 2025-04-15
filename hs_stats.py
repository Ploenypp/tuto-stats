from math import *
from collections import Counter

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

def variance(data, correction = True) :
    # correction : True -> sample variance / False -> population variance
    m = mean(data)
    sum = fsum([(x - m)**2 for x in data])
    if correction : return sum/(len(data)-1)
    return sum/len(data)

def standard_deviation(data, var = True) :
    # var : True -> sample variance / False -> population variance
    if var : return sqrt(variance(data, True))
    return sqrt(variance(data, False))

def z_score(data,x) :
    return (x-mean(data))/standard_deviation(data)