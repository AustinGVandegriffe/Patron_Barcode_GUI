import os
import sys
import time

dir = os.getcwd()
os.system(r'C:\Anaconda3\Scripts\pyside2-uic.exe "{0}\{1}" -o "{0}\{2}" -x'.format(dir,sys.argv[1],sys.argv[2]))

# while sys.argv[2] not in os.listdir():
#     time.sleep(1)

with open(f"{dir}\{sys.argv[2]}","r+") as fin:
    tmp = fin.readlines()
    fin.seek(0,0)
    line = "from PySide2 import QtCore, QtGui, QtWidgets\n"
    index = tmp.index(line)

    fin.write(''.join(tmp[:index-1]))
    fin.write(f'''
###############################################################
# ADDED 2019-07-12 BY AUSTIN VANDEGRIFFE FROM https://stackoverflow.com/a/53237231
import sys,os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
###############################################################

''')
    fin.write(''.join(tmp[index:]))

