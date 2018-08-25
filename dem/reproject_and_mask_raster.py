"""
This script reprojects a raster using an epsg_code and applies a specified mask in ESRI shapefile format

Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB
Licence     : MIT (Latest)
"""
import os
from sys import argv, exit, stdout

resolution, epsg_code = argv[1], argv[2]

# reprojecting the raster
input_tif = "out/output_dem/srtm_90m.tif"
output_tif = "../Data/blue_nile_{0}_dem.tif".format(resolution)
mask_ = "{1}/mask/blue_nile_{0}.shp".format(3395, os.getcwd())
no_data = "-32768"

if not os.path.isdir("../Data/"):
    os.makedirs("../Data/")

print("\n     >>  reprojecting and masking digital elevation model\n\t     saving to {0}\n\n".format(output_tif))
stdout.write("     >>  ")
os.system("gdalwarp -r mode -t_srs EPSG:{0} -tr {1} -{1} -dstnodata {2} -ot Int32 -of GTiff -cutline {3} -crop_to_cutline {4} {5} -overwrite".format(epsg_code, resolution, no_data, mask_, input_tif, output_tif))
