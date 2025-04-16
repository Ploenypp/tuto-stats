from math import *

def permutation(n, r, replacement = False) :
    if replacement : return n**r
    return factorial(n)/factorial(n-r)

def combination(n, r, replacement = False) :
    if replacement : return factorial(n-1+r)/((factorial(r)*factorial(n-1)))
    return factorial(n)/(factorial(r)*factorial(n-r))