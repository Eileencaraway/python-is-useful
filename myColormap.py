#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

"""

Example: suppose you want red to increase from 0 to 1 over the bottom
half, green to do the same over the middle half, and blue over the top
half.  Then you would use:

cdict = {'red':   ((0.0,  0.0, 0.0),
                   (0.5,  1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'green': ((0.0,  0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.75, 1.0, 1.0),
                   (1.0,  1.0, 1.0)),

         'blue':  ((0.0,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (1.0,  1.0, 1.0))}

If, as in this example, there are no discontinuities in the r, g, and b
components, then it is quite simple: the second and third element of
each tuple, above, is the same--call it "y".  The first element ("x")
defines interpolation intervals over the full range of 0 to 1, and it
must span that whole range.  In other words, the values of x divide the
0-to-1 range into a set of segments, and y gives the end-point color
values for each segment.
If there are discontinuities, then it is a little more complicated.
Label the 3 elements in each row in the cdict entry for a given color as
(x, y0, y1).  Then for values of x between x[i] and x[i+1] the color
value is interpolated between y1[i] and y0[i+1].

Going back to the cookbook example, look at cdict['red']; because y0 !=
y1, it is saying that for x from 0 to 0.5, red increases from 0 to 1,
but then it jumps down, so that for x from 0.5 to 1, red increases from
0.7 to 1.  Green ramps from 0 to 1 as x goes from 0 to 0.5, then jumps
back to 0, and ramps back to 1 as x goes from 0.5 to 1.

row i:   x  y0  y1
                /
               /
row i+1: x  y0  y1

Above is an attempt to show that for x in the range x[i] to x[i+1], the
interpolation is between y1[i] and y0[i+1].  So, y0[0] and y1[-1] are
never used.

"""

####################################
cdictB = {'red':   ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),
          
          'blue':  ((0.0, 1.0, 1.0),
                   (1.0, 0.0, 0.0))
        }

myBlues = LinearSegmentedColormap('myBlues', cdictB)
####################################

####################################
cdictBlGr = {'red':   ((0.0, 0.0, 0.0),
                       (1.0, 1.0, 1.0)),
             
             'green': ((0.0, 0.0, 0.0),
                       (1.0, 1.0, 1.0)),
             
             'blue':  ((0.0, 0.4, 0.4),
                       (0.001, 0.0, 0.0),
                       (1.0, 1.0, 1.0))
         }

myBlGr = LinearSegmentedColormap('myBlGr', cdictBlGr)
####################################

####################################
cdictGaps = {'red':   ((0.0, 0.1, 0.1),
                       (0.33, 0.7, 0.7),
                       (0.66, 1, 1),
                       (1.0, 1.0, 1.0)),
             
             'green': ((0.0, 0.1, 0.1),
                       (0.33, 0.7, 0.7),
                       (0.66, 0.05, 0.05),
                       (1.0, 1., 1.)),
             
             'blue':  ((0.0, 0.1, .1),
                       (0.33, 0.01, 0.01),
                       (0.66, 0.05, 0.05),
                       (1.0, 1, 1))
         }

myGaps = LinearSegmentedColormap('myGaps', cdictGaps)
####################################

####################################
cdictBlYl = {'red':   ((0.0, 0.0, 0.0),
                       (0.001, 1.0, 1.0),
                       (1.0, 1.0, 1.0)),
             
             'green': ((0.0, 0.0, 0.0),
                       (0.001, 1.0, 1.0),
                       (1.0, 1.0, 1.0)),
             
             'blue':  ((0.0, 0.4, 0.4),
                       (0.001, 0., 0.),
                       (1.0, 1.0, 1.0))
         }

myBlYl = LinearSegmentedColormap('myBlYl', cdictBlYl)
####################################

####################################
cdictGr = {'red':   ((0.0, 0.2, 0.2),
                     (1.0, 0.0, 0.0)),
             
           'green': ((0.0, 0.2, 0.2),
                     (1.0, 0.0, 0.0)),
           
           'blue':  ((0.0, 0.2, 0.2),
                     (1.0, 0.0, 0.0))
         }

myGr = LinearSegmentedColormap('myGr', cdictGr)
####################################

####################################
# Corey's colormap
cdictcm2 = {'red':  ((0.0, 0.0, 0.0),
                     (0.015873015873, 0.09090909, 0.09090909),
                     (0.031746031746, 0.18181819, 0.18181819),
                     (0.047619047619, 0.27272728, 0.27272728),
                     (0.0634920634921, 0.36363637, 0.36363637),
                     (0.0793650793651, 0.45454547, 0.45454547),
                     (0.0952380952381, 0.54545456, 0.54545456),
                     (0.111111111111, 0.63636363, 0.63636363),
                     (0.126984126984, 0.72727275, 0.72727275),
                     (0.142857142857, 0.81818181, 0.81818181),
                     (0.15873015873, 0.90909094, 0.90909094),
                     (0.174603174603, 1.0, 1.0),
                     (0.190476190476, 0.9285714, 0.9285714),
                     (0.206349206349, 0.85714287, 0.85714287),
                     (0.222222222222, 0.78571427, 0.78571427),
                     (0.238095238095, 0.71428573, 0.71428573),
                     (0.253968253968, 0.64285713, 0.64285713),
                     (0.269841269841, 0.5714286, 0.5714286),
                     (0.285714285714, 0.5, 0.5),
                     (0.301587301587, 0.42857143, 0.42857143),
                     (0.31746031746, 0.35714287, 0.35714287),
                     (0.333333333333, 0.2857143, 0.2857143),
                     (0.349206349206, 0.21428572, 0.21428572),
                     (0.365079365079, 0.14285715, 0.14285715),
                     (0.380952380952, 0.07142857, 0.07142857),
                     (0.396825396825, 0.0, 0.0),
                     (0.412698412698, 0.0, 0.0),
                     (0.428571428571, 0.0, 0.0),
                     (0.444444444444, 0.0, 0.0),
                     (0.460317460317, 0.0, 0.0),
                     (0.47619047619, 0.0, 0.0),
                     (0.492063492063, 0.0, 0.0),
                     (0.507936507937, 0.1, 0.1),
                     (0.52380952381, 0.2, 0.2),
                     (0.539682539683, 0.30000001, 0.30000001),
                     (0.555555555556, 0.40000001, 0.40000001),
                     (0.571428571429, 0.5, 0.5),
                     (0.587301587302, 0.60000002, 0.60000002),
                     (0.603174603175, 0.69999999, 0.69999999),
                     (0.619047619048, 0.80000001, 0.80000001),
                     (0.634920634921, 0.89999998, 0.89999998),
                     (0.650793650794, 1.0, 1.0),
                     (0.666666666667, 0.9929412, 0.9929412),
                     (0.68253968254, 0.98588234, 0.98588234),
                     (0.698412698413, 0.97882354, 0.97882354),
                     (0.714285714286, 0.97176468, 0.97176468),
                     (0.730158730159, 0.96470588, 0.96470588),
                     (0.746031746032, 0.95764709, 0.95764709),
                     (0.761904761905, 0.95058823, 0.95058823),
                     (0.777777777778, 0.94352943, 0.94352943),
                     (0.793650793651, 0.93647057, 0.93647057),
                     (0.809523809524, 0.92941177, 0.92941177),
                     (0.825396825397, 0.93529415, 0.93529415),
                     (0.84126984127, 0.94117647, 0.94117647),
                     (0.857142857143, 0.9470588, 0.9470588),
                     (0.873015873016, 0.95294118, 0.95294118),
                     (0.888888888889, 0.95882356, 0.95882356),
                     (0.904761904762, 0.96470588, 0.96470588),
                     (0.920634920635, 0.97058821, 0.97058821),
                     (0.936507936508, 0.97647059, 0.97647059),
                     (0.952380952381, 0.98235297, 0.98235297),
                     (0.968253968254, 0.98823529, 0.98823529),
                     (0.984126984127, 0.99411762, 0.99411762),
                     (1.0, 1.0, 1.0)),
                     
            'green':((0.0, 0.0, 0.0),
                     (0.015873015873, 0.0, 0.0),
                     (0.031746031746, 0.0, 0.0),
                     (0.047619047619, 0.0, 0.0),
                     (0.0634920634921, 0.0, 0.0),
                     (0.0793650793651, 0.0, 0.0),
                     (0.0952380952381, 0.0, 0.0),
                     (0.111111111111, 0.0, 0.0),
                     (0.126984126984, 0.0, 0.0),
                     (0.142857142857, 0.0, 0.0),
                     (0.15873015873, 0.0, 0.0),
                     (0.174603174603, 0.0, 0.0),
                     (0.190476190476, 0.07142857, 0.07142857),
                     (0.206349206349, 0.14285715, 0.14285715),
                     (0.222222222222, 0.21428572, 0.21428572),
                     (0.238095238095, 0.2857143, 0.2857143),
                     (0.253968253968, 0.35714287, 0.35714287),
                     (0.269841269841, 0.42857143, 0.42857143),
                     (0.285714285714, 0.5, 0.5),
                     (0.301587301587, 0.5714286, 0.5714286),
                     (0.31746031746, 0.64285713, 0.64285713),
                     (0.333333333333, 0.71428573, 0.71428573),
                     (0.349206349206, 0.78571427, 0.78571427),
                     (0.365079365079, 0.85714287, 0.85714287),
                     (0.380952380952, 0.9285714, 0.9285714),
                     (0.396825396825, 1.0, 1.0),
                     (0.412698412698, 1.0, 1.0),
                     (0.428571428571, 1.0, 1.0),
                     (0.444444444444, 1.0, 1.0),
                     (0.460317460317, 1.0, 1.0),
                     (0.47619047619, 1.0, 1.0),
                     (0.492063492063, 1.0, 1.0),
                     (0.507936507937, 1.0, 1.0),
                     (0.52380952381, 1.0, 1.0),
                     (0.539682539683, 1.0, 1.0),
                     (0.555555555556, 1.0, 1.0),
                     (0.571428571429, 1.0, 1.0),
                     (0.587301587302, 1.0, 1.0),
                     (0.603174603175, 1.0, 1.0),
                     (0.619047619048, 1.0, 1.0),
                     (0.634920634921, 1.0, 1.0),
                     (0.650793650794, 1.0, 1.0),
                     (0.666666666667, 0.96941179, 0.96941179),
                     (0.68253968254, 0.93882352, 0.93882352),
                     (0.698412698413, 0.90823531, 0.90823531),
                     (0.714285714286, 0.87764704, 0.87764704),
                     (0.730158730159, 0.84705883, 0.84705883),
                     (0.746031746032, 0.81647062, 0.81647062),
                     (0.761904761905, 0.78588235, 0.78588235),
                     (0.777777777778, 0.75529414, 0.75529414),
                     (0.793650793651, 0.72470587, 0.72470587),
                     (0.809523809524, 0.69411767, 0.69411767),
                     (0.825396825397, 0.63627452, 0.63627452),
                     (0.84126984127, 0.57843137, 0.57843137),
                     (0.857142857143, 0.52058828, 0.52058828),
                     (0.873015873016, 0.4627451, 0.4627451),
                     (0.888888888889, 0.40490198, 0.40490198),
                     (0.904761904762, 0.34705883, 0.34705883),
                     (0.920634920635, 0.28921568, 0.28921568),
                     (0.936507936508, 0.23137255, 0.23137255),
                     (0.952380952381, 0.17352942, 0.17352942),
                     (0.968253968254, 0.11568628, 0.11568628),
                     (0.984126984127, 0.05784314, 0.05784314),
                     (1.0, 0.0, 0.0)),
            
            'blue': ((0.0, 1.0, 1.0),
                     (0.015873015873, 1.0, 1.0),
                     (0.031746031746, 1.0, 1.0),
                     (0.047619047619, 1.0, 1.0),
                     (0.0634920634921, 1.0, 1.0),
                     (0.0793650793651, 1.0, 1.0),
                     (0.0952380952381, 1.0, 1.0),
                     (0.111111111111, 1.0, 1.0),
                     (0.126984126984, 1.0, 1.0),
                     (0.142857142857, 1.0, 1.0),
                     (0.15873015873, 1.0, 1.0),
                     (0.174603174603, 1.0, 1.0),
                     (0.190476190476, 1.0, 1.0),
                     (0.206349206349, 1.0, 1.0),
                     (0.222222222222, 1.0, 1.0),
                     (0.238095238095, 1.0, 1.0),
                     (0.253968253968, 1.0, 1.0),
                     (0.269841269841, 1.0, 1.0),
                     (0.285714285714, 1.0, 1.0),
                     (0.301587301587, 1.0, 1.0),
                     (0.31746031746, 1.0, 1.0),
                     (0.333333333333, 1.0, 1.0),
                     (0.349206349206, 1.0, 1.0),
                     (0.365079365079, 1.0, 1.0),
                     (0.380952380952, 1.0, 1.0),
                     (0.396825396825, 1.0, 1.0),
                     (0.412698412698, 0.83333331, 0.83333331),
                     (0.428571428571, 0.66666669, 0.66666669),
                     (0.444444444444, 0.5, 0.5),
                     (0.460317460317, 0.33333334, 0.33333334),
                     (0.47619047619, 0.16666667, 0.16666667),
                     (0.492063492063, 0.0, 0.0),
                     (0.507936507937, 0.0, 0.0),
                     (0.52380952381, 0.0, 0.0),
                     (0.539682539683, 0.0, 0.0),
                     (0.555555555556, 0.0, 0.0),
                     (0.571428571429, 0.0, 0.0),
                     (0.587301587302, 0.0, 0.0),
                     (0.603174603175, 0.0, 0.0),
                     (0.619047619048, 0.0, 0.0),
                     (0.634920634921, 0.0, 0.0),
                     (0.650793650794, 0.0, 0.0),
                     (0.666666666667, 0.01254902, 0.01254902),
                     (0.68253968254, 0.02509804, 0.02509804),
                     (0.698412698413, 0.03764706, 0.03764706),
                     (0.714285714286, 0.05019608, 0.05019608),
                     (0.730158730159, 0.0627451, 0.0627451),
                     (0.746031746032, 0.07529412, 0.07529412),
                     (0.761904761905, 0.08784314, 0.08784314),
                     (0.777777777778, 0.10039216, 0.10039216),
                     (0.793650793651, 0.11294118, 0.11294118),
                     (0.809523809524, 0.1254902, 0.1254902),
                     (0.825396825397, 0.11503269, 0.11503269),
                     (0.84126984127, 0.10457517, 0.10457517),
                     (0.857142857143, 0.09411766, 0.09411766),
                     (0.873015873016, 0.08366013, 0.08366013),
                     (0.888888888889, 0.07320262, 0.07320262),
                     (0.904761904762, 0.0627451, 0.0627451),
                     (0.920634920635, 0.05228759, 0.05228759),
                     (0.936507936508, 0.04183007, 0.04183007),
                     (0.952380952381, 0.03137255, 0.03137255),
                     (0.968253968254, 0.02091503, 0.02091503),
                     (0.984126984127, 0.01045752, 0.01045752),
                     (1.0, 0.0, 0.0))
        }

mycm2 = LinearSegmentedColormap('mycm2', cdictcm2)
####################################