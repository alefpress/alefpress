#!/usr/bin/env python
from PIL import Image,ImageMath
import os
import unittest
import sys
import scribus
import subprocess
try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

margins = (10, 10, 10, 30)

def main1():
     path=os.getcwd()
     openDoc(path + "/slas/test_text_LTR.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + "/out/LTR_left.png"
     i.save()
     closeDoc()

     openDoc(path + "/slas/test_text_center.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + "/out/LTR_center.png"
     i.save()
     closeDoc()

     openDoc(path + "/slas/test_text_right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/LTR_right.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/test_text_justified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/LTR_justifid.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/test_text_Forcedjustified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/LTR_Forcedjustified.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RTL_left.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RTL_left.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RTL_center.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RTL_center.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RTL_right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RTL_right.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RTL_justified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RTL_justified.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RTL_forcedjustified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RTL_forcedjustified.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/FixedLI_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FixedLI_Book.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/FixedLI_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FixedLI_Bold.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/FixedLI_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FixedLI_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/FixedLI_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FixedLI_Oblique.png'
     i.save()
     closeDoc()

     ##font text
     openDoc(path + "/slas/Auto_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Auto_Book.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/Auto_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Auto_Bold.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/Auto_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Auto_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/Auto_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Auto_Oblique.png'
     i.save()
     closeDoc()

      ##colerd text
     openDoc(path + "/slas/GreenCol_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/GreenCol_Bold.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/RedCol_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/RedCol_Book.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/BuleCol_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/BuleCol_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc(path + "/slas/yellowCol_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/yellowCol_Oblique.png'
     i.save()
     closeDoc()

     ##Fill textbox
     openDoc(path + "/slas/FillGreen_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FillGreen_Book.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/FillMagenta_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FillMagenta_Bold.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/FillBlue_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FillBlue_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/FillYellow_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/FillYellow_BoldOblique.png'
     i.save()
     closeDoc()
     
     ##DropCaps
     openDoc(path + "/slas/DropCaps_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DropCaps_Book.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DropCaps_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DropCaps_Bold.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DrpoCaps_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DrpoCaps_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DropCaps_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DropCaps_BoldOblique.png'
     i.save()
     closeDoc()
     
     
     ##drop shadow
     openDoc(path + "/slas/DS_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DS_Book.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DS_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DS_Bold.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DS_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DS_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc(path + "/slas/DS_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/DS_BoldOblique.png'
     i.save()
     closeDoc()
     
     ##column intext
     openDoc(path + "/slas/col_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/col_text.png'
     i.save()
     closeDoc()
     
     ##offset of baseline characters
     openDoc(path + "/slas/Offset_baseline_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Offset_baseline_char.png'
     i.save()
     closeDoc()
     
     ##manual tracking
     openDoc(path + "/slas/Manual_Tracking.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Manual_Tracking.png'
     i.save()
     closeDoc()
     
     ##scaling width of characters
     openDoc(path + "/slas/scaling_width_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/scaling_width_char.png'
     i.save()
     closeDoc()
     
     ##scaling hight of characters
     openDoc(path + "/slas/scaling_hight_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/scaling_hight_char.png'
     i.save()
     closeDoc()
     
     ##word tracking min
     openDoc(path + "/slas/word_tracking_min.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/word_tracking_min.png'
     i.save()
     closeDoc()
     
     ##word tracking norm
     openDoc(path + "/slas/word_tracking_norm.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/word_tracking_norm.png'
     i.save()
     closeDoc()
     
     ##Glyph extension max
     openDoc(path + "/slas/Glyph_extension_max.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Glyph_extension_max.png'
     i.save()
     closeDoc()
     
     ##Glyph extension min
     openDoc(path + "/slas/Glyph_extension_min.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Glyph_extension_min.png'
     i.save()
     closeDoc()
     
     ##OPtical Margins Both Side
     openDoc(path + "/slas/optical_margins_BothSide.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/optical_margins_BothSide.png'
     i.save()
     closeDoc()
     
     ##OPtical Margins Left Side
     openDoc(path + "/slas/optical_margins_Left.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/optical_margins_Left.png'
     i.save()
     closeDoc()
     
     ##OPtical Margins Right Side
     openDoc(path + "/slas/optical_margins_Right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/optical_margins_Right.png'
     i.save()
     closeDoc()
     
     ##Hyphenation
     openDoc(path + "/slas/Hyphenation.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Hyphenation.png'
     i.save()
     closeDoc()
     
     ##Path text properties
     openDoc(path + "/slas/Path_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Path_text.png'
     i.save()
     closeDoc()
     
     #Orphans and widows keep next paragraph
     openDoc(path + "/slas/Orphans_Widows_KeepNextParagraph.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Orphans_Widows_KeepNextPar.png'
     i.save()
     closeDoc()
     
     #Orphans and widows do not split paragraph
     openDoc(path + "/slas/Orphans_Widows_DoNotSplit.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/Orphans_Widows_DoNotSplit.png'
     i.save()
     closeDoc()
     
     #star Test
     openDoc(path + "/slas/Star_test.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/star_test.png'
     i.save()
     closeDoc()
     
     #polygon Test
     openDoc(path + "/slas/test_polygon.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/polygon.png'
     i.save()
     closeDoc()
     
     #insert picture in image Frame Test
     openDoc(path + "/slas/imageFrame.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/imageFrame.png'
     i.save()
     closeDoc()
     
     #table test
     openDoc(path + "/slas/table_test.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/table_test.png'
     i.save()
     closeDoc()
     
     #underLine_word
     openDoc(path + "/slas/underLine_word.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/underLine_word.png'
     i.save()
     closeDoc()
     
     #underLine_text
     openDoc(path + "/slas/underLine_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/underLine_text.png'
     i.save()
     closeDoc() 
     
     
     #all Caps
     openDoc(path + "/slas/allCaps.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/allCaps.png'
     i.save()
     closeDoc() 
     
     #small Caps
     openDoc(path + "/slas/smallCaps.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/smallCaps.png'
     i.save()
     closeDoc() 
     
      #strike out
     openDoc(path + "/slas/strikOut.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = path + '/out/strikOut.png'
     i.save()
     closeDoc()
     
if __name__ == '__main__':
    main1()
