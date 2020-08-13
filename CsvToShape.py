# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:22:09 2020

@author: Lina
"""


import arcpy
arcpy.env.overwriteOutput = True
from os import listdir
from os.path import isfile, join, basename

csvpath = r'C:\Test\Testmapp'
outshapefolder = r'C:\Test\Outputshapes'

files = [join(csvpath,f) for f in listdir(csvpath) if isfile(join(csvpath, f))]

for f in files:
    arcpy.MakeTableView_management(in_table=f, out_view='tempview')
    arcpy.MakeXYEventLayer_management(table='tempview', in_x_field='Lat', in_y_field='Lon', 
                                     out_layer='tempevent', spatial_reference=4326)
    arcpy.CopyFeatures_management(in_features='tempevent', out_feature_class=join(outshapefolder,basename(f).replace('.csv','.shp')))