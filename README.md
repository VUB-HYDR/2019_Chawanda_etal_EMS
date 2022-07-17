# Data Preparation for 2019_Chawanda_etal_EMS
Scripts used to process data and namelist for QSWAT Workflow.
Find the QSWAT Workflow v1.5.8 [here](https://github.com/VUB-HYDR/QSWAT_Automated_Workflow)

## To Install
[gdal](https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows)   
 
## For users
This repository includes the scripts that automatically downloads SRTM data for Blue Nile area and processes it for use with QSWAT Workflow v1.5.8.
It also has script to process ESA land use data downloaded from [http://maps.elie.ucl.ac.be/CCI/viewer/download.php](http://maps.elie.ucl.ac.be/CCI/viewer/download.php) for the Blue Nile area. In This case, the 2009 land use map (ESACCI-LC-L4-LCCS-Map-300m-P1Y-2009-v2.0.7.tif) was used.
There is also a script that processes the FAO soil data downloaded from [FAO's website](https://storage.googleapis.com/fao-maps-catalog-data/uuid/446ed430-8383-11db-b9b2-000d939bc5d8/resources/DSMW.zip). The Shapefile from this data should be placed in [DSMW](./soil/DSMW) folder.

### 1. [prepare_data.py](./prepare_data.py) 
This is the file used to launch the data preparation process. You can also independently run the script in the directories as described below.

### 2. [dem/main.py](./dem/main.py)
This is script that coordinates the download and processing of SRTM Data for the Blue Nile

### 3. [land_use/clip_land_use.py](./land_use/clip_land_use.py)
This scripts clips the 2009 ESA land use map to the Blue Nile and reprojects it.

### 4. [soil/process_soil_map.py](./soil/process_soil_map.py)
This script creates a raster map for the Blue Nile from the [FAO soil data](https://storage.googleapis.com/fao-maps-catalog-data/uuid/446ed430-8383-11db-b9b2-000d939bc5d8/resources/DSMW.zip).
The usersoil table used in this script is obtained from the installation of [MWSWAT](http://www.waterbase.org/download_mwswat.html) downloaded from http://www.waterbase.org/download_mwswat.html

### 5. [namelist.py](./namelist.py)
This is the namelist used in setting up the Blue Nile SWAT model presented in Chawanda et al. (2019) using the [QSWAT Workflow v1.5.8](https://github.com/VUB-HYDR/QSWAT_Automated_Workflow).

## Author
[Celray James CHAWANDA](https://github.com/celray/) 

## License
This project is licensed under the MIT License. See also the [license](./LICENSE) file.

