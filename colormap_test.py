# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:07:51 2015

@author: upression1
"""

# ============ Draw map pour test ==================================

import Image
import numpy as np
import scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt


# --------------------

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'
File_Name = str(data_in)+'A20022652002272.L3m_8D_CHL_chlor_a_4km_ZI.npy'
#File_Name = np.dot(File_Name,1.0)
data=np.load(File_Name)
imgplot = plt.imshow((data[1]), interpolation='none')
plt.show()

