import math

def main_r(dim1,dim2):
    ''' Calculates rectangle's area'''
    ar = dim1 * dim2
    return round(ar,2)

def main_tr(dim1,dim2):
    ''' Calculates triangle's area'''
    at = (dim1 * dim2)/2
    return round(at,2)

def main_c(rad):
    ''' Calculates circle's area'''
    ac = (math.pi)*pow(rad,2)
    return round(ac,2)
