import time
import rename
from measure import *
from coords import *
from downloader import get_downloaders
from cutter import cut_all

dws = get_downloaders(coords)
download = dws.download
download_all = dws.download_all

path = r'C:\Users\Fewed\Downloads\bus\1'
rename = rename.with_path(path)

time.sleep(3)
#download()
#download_all()
#get_coords()
#rename()
cut_all(path, start=11, end=5)
