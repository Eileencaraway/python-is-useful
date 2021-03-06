#!/usr/bin/env python

import sys
import os
import math
import numpy
from numpy import *
from pylab import *

sys.argv
first = 0
values = 0
sq_values = 0
sum_column = 0


for filename in sys.argv[1:]:
    f = open(filename, 'rb')
    no_column = fromfile(f,'int32',1)
    data = fromfile(f,'float32')
    reform_data=numpy.reshape(data, (-1,no_column))
    if first == 0:
        Sum_List = reform_data
        d = array(reform_data)
        Sqsum_List = d*d
        length = len(Sum_List)
        No_files = 1
        first = 1
       
    else:
        if len(reform_data)==length:
            No_files +=1
            d = array(reform_data)
            Sum_List += d
            Sqsum_List += d*d
            #for i in range(0, len(reform_data)):
             #   Sum_List[i] += reform_data[i]
    
    sys.stderr.write('import '+filename+' size-'+str(len(reform_data))+'\n')
    f.close()

sys.stderr.write('No_files = '+str(No_files)+'\n')
sl = array(Sum_List)
Sumsq_List = sl*sl
computeError = (No_files*Sqsum_List - Sumsq_List)/No_files/No_files


for i in range(0, length):
    for j in range(0, len(Sum_List[i])):
        if computeError[i][j]<0:
            computeError[i][j]= -1.0*computeError[i][j]
        print Sum_List[i][j]/No_files, math.sqrt(computeError[i][j]),
    print
    sum_column += Sum_List[i]
    values = Sum_List[i]
    sq_values += values*values
#print sum_column, sq_values


result = zeros([1, 2*len(Sum_List[0])], 'f'); 
for i in range(0, len(Sum_List[0])):
    average = sum_column[i]/(No_files*length)
    variance = sq_values[i]/(No_files*No_files*length) - average*average
    if variance<0:
        variance = -1.0*variance
    stddev = math.sqrt(variance)
    result[0][2*i] = average
    result[0][2*i+1] = stddev

print "#Meanvalues and #variance = ", 
for j in range(0, len(result[0])):
    print result[0][j],
    
