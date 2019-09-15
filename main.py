import time
import rename
from coords import *
from downloader import get_downloaders
from cutter import cut_all

dws = get_downloaders(coords)
download = dws.download
download_all = dws.download_all

path = r'C:\Users\Fewed\Downloads\Coursera - Machine Learning'
rename = rename.with_path(path)

time.sleep(3)
# download()
# download_all(73)
# get_coords()
rename()
# cut_all(path)
