"""
Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB

this script coordinates the other scripts in processing input data used in Chawanda et al. (2018).
"""
import os

dem_dir = "dem"
dem_script = "main.py"

lu_dir = "land_use"
lu_script = "clip_land_use.py"

soil_dir = "soil"
soil_script = "process_soil_map.py"

print("\n    > processing dem")
os.chdir(dem_dir)
os.system("python {0}".format(dem_script))

print("\n    > processing land use")
os.chdir("../{0}".format(lu_dir))
os.system("python {0}".format(lu_script))

print("\n    > processing soil")
os.chdir("../{0}".format(soil_dir))
os.system("python {0}".format(soil_script))
