# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:05:46 2015

@author: upression1
"""

import os
import sys  
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy

         #------------ Import / lecture npy data
         
data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'
#files = os.lisdir(data_in)
#files.sort()

i = 1       


day= 185
day2= 0
temps = 1

for a in range (2002,2003):
    print a
    while day2 < 248:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366
         
        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_'
        myfile = filen+'ZE'
        print myfile
         
         
         
         #------------ Isoligne
         
         
         
         
         #------------ Affichage