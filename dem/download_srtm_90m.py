"""
reference   : http://dwtkns.com/srtm/
this script downloads SRTM 90m Digital Elevation Database v4.1 for blue nile area

Author      : Celray James CHAWANDA
Email       : celray.chawanda@outlook.com
Institution : VUB
Licence     : MIT (Latest)
"""

import urllib2
import os
import sys
from subprocess import call
import platform

OS = platform.system()

try:
    os.makedirs("raw")
except:
    pass

def append_numbers(list_, start, end, row):
    for i in range(start, end + 1):
        list_.append([i, row])
    return list_

def update_progress(count,end_val, bar_length, cur, total, filename, OS_):   #bar_length=20
    percent = float(count) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = '-' * (bar_length - len(hashes))
    sys.stdout.write("\r\tsrtm file : " + filename + " -- " + str(cur) + " of " + str(total) + " -- percent Complete: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    if OS_ == "Windows":
        print("")

base_url = "http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/"
print("\tdownloading zipped tiff files from http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/")
print("\tsaving to " + os.getcwd() + "/raw")
tiles = []
tiles = append_numbers(tiles, 43, 45, 9) #(column start, column end, row)
tiles = append_numbers(tiles, 43, 45, 10)
tiles = append_numbers(tiles, 43, 46, 11)

url_list = []
pwd = os.getcwd()
for element in tiles:
    url_list.append(base_url + "srtm_" + str(element[0]) + "_" + (
        str(element[1]) if element[1] >= 10 else ("0" + str(element[1]))) + ".zip")

count = 0
end = len(url_list)
os.chdir("raw")
for remote_file in url_list:
    count += 1  
    if os.path.isfile(remote_file.split('/')[-1]):
        if int(os.path.getsize(remote_file.split('/')[-1])) <= 26000:
            os.remove(remote_file.split('/')[-1])
            if OS == "Windows":
                os.system("curl -O {0}".format(remote_file))
            else:
                os.system("wget -q " + remote_file)
                update_progress(count, end, 22, count, end, remote_file.split('/')[-1], OS)
            continue
        else:
            #update_progress(count, end, 22, count, end, remote_file.split('/')[-1], OS)
            continue
    else:
        if OS == "Windows":
            os.system("curl -O {0}".format(remote_file))            
        else:
            os.system("wget -q " + remote_file)
            update_progress(count, end, 18, count, end, remote_file.split('/')[-1], OS)

os.chdir(pwd)
print("\n")

