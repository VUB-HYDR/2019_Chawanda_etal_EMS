"""
This script merges raster tiles and resamples them to a desired
resolution the merging is done in batches due to gdal limitations
in number of arguments

Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB
Licence     : MIT (Latest)
"""

import os
from glob import glob
from sys import argv, exit, stdout

def list_files_from(folder, extension):
    if folder.endswith("/"):
        list_of_files = glob(folder + "*." + extension)
    else:
        list_of_files = glob(folder + "/*." + extension)
    return list_of_files

nodataval   = "-32768"

try:
    os.makedirs("out/merged_parts")
except:
    pass
try:
    os.makedirs("out/output_dem")
except:
    pass

all_tifs = list_files_from("out/extracted", "tif")
part_delta = len(all_tifs)/2

if part_delta <= 1:
    print("\t !!  too few raster tiles to work on; a minimum is 14")
    exit()

part_1 = all_tifs[0:part_delta]
part_2 = all_tifs[part_delta:(part_delta*2)]

print("     >  creating merged parts")
stdout.write("\t    ")

if not os.path.isfile("out/merged_parts/part_1.tif"):
    os.system("gdalwarp " + " ".join(str(x) for x in part_1) + " " + "out/merged_parts/part_1.tif -srcnodata " + nodataval + " -dstnodata " + nodataval)
if not os.path.isfile("out/merged_parts/part_2.tif"):
    os.system("gdalwarp " + " ".join(str(x) for x in part_2) + " " + "out/merged_parts/part_2.tif -srcnodata " + nodataval + " -dstnodata " + nodataval)
print("")

# the big merge
print("     !> merging parts to final raster")
stdout.write("        ")

if not os.path.isfile("out/output_dem/srtm_90m.tif"):
    os.system("gdalwarp " + " ".join(str(x) for x in list_files_from("out/merged_parts/", "tif")) + " " + "out/output_dem/srtm_90m.tif -srcnodata " + nodataval + " -dstnodata " + nodataval)


