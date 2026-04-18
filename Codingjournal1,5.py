# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:14:46 2026

@author: wiley
"""


from astropy.table import Table
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)

y = np.sin(x)

data = Table([x,y],names=['x','y'])
def main():
    print(data)
    
if __name__ =='__main__':
    main()


