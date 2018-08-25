import zipfile, os, sys
from glob import glob

def update_progress(count,end_val, bar_length):   #bar_length=20
    percent = float(count) / end_val
    hashes = "#" * int(round(percent * bar_length))
    spaces = '_' * (bar_length - len(hashes))
    sys.stdout.write("\r\tpercent Complete: [{0}] {1}%".format(hashes + spaces, float(round(percent * 100, 2)) if str(float(round(percent * 100, 2)))[-2:-1] != "." else str(float(round(percent * 100, 2))) + "0"))
    sys.stdout.flush()

def list_files_from(folder, extension):
    if folder.endswith("/"):
        list_of_files = glob(folder + "*." + extension)
    else:
        list_of_files = glob(folder + "/*." + extension)
    return list_of_files

cwd = os.getcwd()
Zipped_list = list_files_from(cwd + "/raw", "zip")
count = 1
print("\tunzipping srtm data")
for zip_file in Zipped_list:
    zip_ref = zipfile.ZipFile(zip_file, 'r')
    if os.path.isfile(cwd + "/out/extracted/" + zip_file.split("/")[-1].split(".")[0] + ".tif"):
        update_progress(count,len(Zipped_list), 62)
        count += 1
        continue
    zip_ref.extractall(cwd + "/out/extracted")
    zip_ref.close()
    update_progress(count,len(Zipped_list), 72)
    count += 1

print ("\n")
