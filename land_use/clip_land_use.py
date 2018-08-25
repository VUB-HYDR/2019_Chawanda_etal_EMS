"""
This script clips the 2009 ESA land cover map and reprojects it to EPSG 3395

Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB
Licence     : MIT (Latest)
"""
import os, sys
from shutil import copyfile

if not os.path.isdir("../Data/"):
    os.makedirs("../Data/")

copyfile("land_lookup.csv", "../Data/land_lookup.csv")

resolution = 300
epsg_code = 32637

# reprojecting the raster
input_tif = "ESACCI-LC-L4-LCCS-Map-300m-P1Y-2009-v2.0.7.tif"
output_tif = " ../Data/blue_nile_{0}_land_use.tif".format(str(resolution).replace(".", "_"))
print("     >> reprojecting raster {0} to EPSG:{1}".format(input_tif, str(epsg_code)))

# apply mask
mask_ = "{0}/mask/blue_nile_3395.shp".format(os.getcwd())
print("        and applying mask, {0}".format(mask_))
sys.stdout.write("\t     ")

os.system("gdalwarp -r mode -t_srs EPSG:{0} -tr {1} -{1} -dstnodata -32768 -ot Int32 -of GTiff -cutline {2} -crop_to_cutline {3} {4} -overwrite".format(epsg_code, resolution, mask_, input_tif, output_tif))
