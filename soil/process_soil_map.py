"""
Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB

this script coordinates the other scripts in processing soil data downloaded from http://www.waterbase.org/download_data.html
use under MIT licence
"""
import os, osr
import sys
import pyodbc
import csv
from dbfpy import dbf
from glob import glob

def dbf_to_csv(out_table):#Input a dbf, output a csv
    csv_fn = out_table[:-4]+ ".csv" #Set the table as .csv format
    with open(csv_fn,'wb') as csvfile: #Create a csv file and write contents from dbf
        in_db = dbf.Dbf(out_table)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields: #Write headers
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db: #Write records
            out_csv.writerow(rec.fieldData)
        in_db.close()
    dbf_content = read_from(csv_fn)
    return dbf_content

def extract_table_from_mdb(mdb_path,table,output_file):
    # set up some constants
    DRV = '{Microsoft Access Driver (*.mdb)}'; PWD = 'pw'

    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,mdb_path,PWD))
    cur = con.cursor()

    # run a query and get the results 
    SQL = 'SELECT * FROM ' + table + ';' # your query goes here
    rows = cur.execute(SQL).fetchall()

    cur.close()
    con.close()
    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    with open(output_file, 'wb') as fou:
        csv_writer = csv.writer(fou) # default field-delimiter is ","
        csv_writer.writerows(rows)

    table_contents = read_from(output_file)
    return table_contents

def read_from(filename):
    g = open(filename, 'r')
    file_text = g.readlines()
    return file_text
    g.close

def write_to(filename,text_to_write):
    g = open(filename, 'w')
    g.write(text_to_write)
    g.close

if not os.path.isdir("../Data/"):
    os.makedirs("../Data/")  # create output directory

# clip shapefile
if not os.path.isdir("tmp"):
    os.makedirs("tmp")  # create temporary output directory

mask = "mask/blue_nile.shp"

all_soils = "DSMW/DSMW.shp"
zone_soils = "tmp/blue_nile.shp"
    # assign projection

prj_ = osr.SpatialReference()
prj_.ImportFromEPSG(4326)
#print("\t >>  {0}".format(prj_))
prj_wkt = prj_.ExportToWkt()
write_to("tmp/blue_nile.prj", prj_wkt)

print("     !> cliping to {0} by mask".format(mask))
os.system("ogr2ogr -clipsrc {0} {1} {2}".format(mask, zone_soils, all_soils))

# rasterise the resulting vector
value_field = "SNUM"
raster_resolution = 0.002242152
extent_ = "32.400000000000006 7.499999999999393 40.50000000000001 16.099999999999074"
output_raster = "tmp/blue_nile_soil.tif"

print("     >  creating raster, {0}".format(output_raster))

sys.stdout.write("        ")
os.system("gdal_rasterize -a {0} -tr {1} {1} -a_nodata 0.0 -te {2} -ot Int32 -of GTiff {3} {4}".format(value_field, raster_resolution, extent_, zone_soils, output_raster))

# extracting soil map attribute table
print("\n     >> extracting tables")
usersoil = extract_table_from_mdb("mwswat2012.mdb", "usersoil", "tmp/usersoil.tmp~")
dbf_contents = dbf_to_csv("{0}.dbf".format(zone_soils[:-4]))

# create soil lookup
lookup_string = "SOIL_ID,NAME\n"
usersoil_string = "OBJECTID,MUID,SEQN,SNAM,S5ID,CMPPCT,NLAYERS,HYDGRP,SOL_ZMX,ANION_EXCL,SOL_CRK,TEXTURE,SOL_Z1,SOL_BD1,SOL_AWC1,SOL_K1,SOL_CBN1,CLAY1,SILT1,SAND1,ROCK1,SOL_ALB1,USLE_K1,SOL_EC1,SOL_Z2,SOL_BD2,SOL_AWC2,SOL_K2,SOL_CBN2,CLAY2,SILT2,SAND2,ROCK2,SOL_ALB2,USLE_K2,SOL_EC2,SOL_Z3,SOL_BD3,SOL_AWC3,SOL_K3,SOL_CBN3,CLAY3,SILT3,SAND3,ROCK3,SOL_ALB3,USLE_K3,SOL_EC3,SOL_Z4,SOL_BD4,SOL_AWC4,SOL_K4,SOL_CBN4,CLAY4,SILT4,SAND4,ROCK4,SOL_ALB4,USLE_K4,SOL_EC4,SOL_Z5,SOL_BD5,SOL_AWC5,SOL_K5,SOL_CBN5,CLAY5,SILT5,SAND5,ROCK5,SOL_ALB5,USLE_K5,SOL_EC5,SOL_Z6,SOL_BD6,SOL_AWC6,SOL_K6,SOL_CBN6,CLAY6,SILT6,SAND6,ROCK6,SOL_ALB6,USLE_K6,SOL_EC6,SOL_Z7,SOL_BD7,SOL_AWC7,SOL_K7,SOL_CBN7,CLAY7,SILT7,SAND7,ROCK7,SOL_ALB7,USLE_K7,SOL_EC7,SOL_Z8,SOL_BD8,SOL_AWC8,SOL_K8,SOL_CBN8,CLAY8,SILT8,SAND8,ROCK8,SOL_ALB8,USLE_K8,SOL_EC8,SOL_Z9,SOL_BD9,SOL_AWC9,SOL_K9,SOL_CBN9,CLAY9,SILT9,SAND9,ROCK9,SOL_ALB9,USLE_K9,SOL_EC9,SOL_Z10,SOL_BD10,SOL_AWC10,SOL_K10,SOL_CBN10,CLAY10,SILT10,SAND10,ROCK10,SOL_ALB10,USLE_K10,SOL_EC10,SOL_CAL1,SOL_CAL2,SOL_CAL3,SOL_CAL4,SOL_CAL5,SOL_CAL6,SOL_CAL7,SOL_CAL8,SOL_CAL9,SOL_CAL10,SOL_PH1,SOL_PH2,SOL_PH3,SOL_PH4,SOL_PH5,SOL_PH6,SOL_PH7,SOL_PH8,SOL_PH9,SOL_PH10\n"

look_up_values = []

for atr_line in dbf_contents:
    atr_line = atr_line.replace("/", "-")
    if atr_line.startswith(value_field):
        continue
    soil_id, soil_name = atr_line.split(",")[0], atr_line.split(",")[1]
    if soil_id in look_up_values:
        continue
    else:
        look_up_values.append(soil_id)
        for usersoil_line in usersoil:
            indicator = ""
            user_soil_name = usersoil_line.split(",")[3]
            if not user_soil_name.split("-")[0] == soil_name.split("-")[0]:
                continue
            if user_soil_name.startswith(soil_name):
                lookup_string +="{0},{1}\n".format(soil_id, user_soil_name)
                usersoil_string += usersoil_line
                indicator = user_soil_name
                break
        if not indicator == "":
            continue
    print "     !! there is a problem in identifying soils,\n\t   please check that the soil names from shape and database are similar"
    sys.exit()



write_to("../Data/usersoil.csv", usersoil_string)
write_to("../Data/soil_lookup.csv", lookup_string)

# reprojecting the raster
resolution = 300
epsg_code = 32637

input_tif = "tmp/blue_nile_soil.tif"
output_tif = "../Data/blue_nile_300_soil.tif"
print("     >> reprojecting raster " + input_tif + " to EPSG:" + str(epsg_code))

# apply mask
#mask_ = os.getcwd() + "/mask/blue_nile.shp"
#print("and applying mask, " + mask_)
sys.stdout.write("     >> ")

os.system("gdalwarp -r mode -t_srs EPSG:" + str(epsg_code) + " -tr " + str(resolution) + " -" + str(resolution) + " -dstnodata " + "-32768" + " -ot " + "Int32" + " -of GTiff -crop_to_cutline " + input_tif + " " + output_tif + " -overwrite") # -cutline " + mask_ + " 
print("\n     >> finnished")

tmp_files = glob("tmp/" + "*")
for tmp_file in tmp_files:
    if os.path.isfile(tmp_file):
        os.remove(tmp_file)
