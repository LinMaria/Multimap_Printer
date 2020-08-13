# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:28:28 2020

@author: Lina
"""

import arcpy, os  
from arcpy import mapping as m  
arcpy.env.overwriteOutput = True  
  
mapPath = r'C:\Users\Lina\Google Drive\Leo\2_SIG\MXD\PruebaBatchMapas\Prueba.mxd'  
outpath = r'C:\Users\Lina\Google Drive\Leo\2_SIG\MXD\PruebaBatchMapas\Exports'  
  
mxd = m.MapDocument(mapPath)  
df = m.ListDataFrames(mxd)[0]  
  
# Loop through layers  
for lyr in m.ListLayers(mxd, 'GMRT3_*'):  
    lyr.visible = True  
    #lyr.showLabels = True # I'm assuming this is where you have the properties?  
    jpg = os.path.join(outpath, lyr.name + '.jpg')  
    m.ExportToJPEG(mxd, jpg)  
    #print('Exported %s') %jpg  
    lyr.visible = False  
          
del mxd  