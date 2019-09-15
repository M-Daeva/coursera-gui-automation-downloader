import time
import rename
from coords import *
from downloader import get_downloaders

dws = get_downloaders(coords)
download = dws.download
download_all = dws.download_all

path = r'C:\Users\Fewed\Downloads\Coursera - Математика и Python для анализа данных\test'
rename = rename.with_path(path)

time.sleep(3)
# download()
download_all(1)
# get_coords()
# rename()
