"""
This script controls the other scripts, use the descriptions there in for explanation

Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB
Licence     : MIT (Latest)
"""

import sys
import os

resolution, epsg_code = 300, 32637 # m, WGS 84/ UTM Zone 37N

# create output folder
try:
    os.mkdir("out/extracted")
except:
    pass

# set the name of the output files and variables

# downloading srtm elevation data
os.system("python download_srtm_90m.py")

# extracting elevation data from raw directory to out/extracted
os.system("python extract_zipped.py")

# merge the extracted raster tiles 
os.system("python merge_in_batches.py")

# mask and resample the extracted raster tiles 
os.system("python reproject_and_mask_raster.py " + str(resolution) + " " + str(epsg_code))
