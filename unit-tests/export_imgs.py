from PIL import Image,ImageMath
import os
import unittest
import scribus
import subprocess

try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

def main1():
   path = 'slas/'
   for file_name in os.listdir(path):
       if file_name.endswith('.sla'):
          openDoc(path + file_name)
          s=file_name.split(".")
          a=s[0]
          i = ImageExport()
          i.type = 'PNG' # select one from i.allTypes list\n\
          i.scale = 100 # I want to have 100%\n\
          i.name = 'out/' + a + '.png'
          i.save()
if __name__ == '__main__':
    main1()
