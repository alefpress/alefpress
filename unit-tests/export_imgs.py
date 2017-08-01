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

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_text_LTR.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/LTR_left.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_text_center.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/LTR_center.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_text_right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/LTR_right.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_text_justified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/LTR_justifid.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_text_Forcedjustified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/LTR_Forcedjustified.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RTL_left.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RTL_left.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RTL_center.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RTL_center.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RTL_right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RTL_right.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RTL_justified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RTL_justified.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RTL_forcedjustified.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RTL_forcedjustified.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FixedLI_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FixedLI_Book.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FixedLI_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FixedLI_Bold.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FixedLI_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FixedLI_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FixedLI_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FixedLI_Oblique.png'
     i.save()
     closeDoc()

     ###font text
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Auto_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Auto_Book.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Auto_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Auto_Bold.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Auto_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Auto_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Auto_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Auto_Oblique.png'
     i.save()
     closeDoc()

      ###colerd text
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/GreenCol_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/GreenCol_Bold.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/RedCol_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/RedCol_Book.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/BuleCol_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/BuleCol_BoldOblique.png'
     i.save()
     closeDoc()

     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/yellowCol_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/yellowCol_Oblique.png'
     i.save()
     closeDoc()

     ###Fill textbox
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FillGreen_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FillGreen_Book.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FillMagenta_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FillMagenta_Bold.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FillBlue_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FillBlue_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/FillYellow_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/FillYellow_BoldOblique.png'
     i.save()
     closeDoc()
     
     ###DropCaps
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DropCaps_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DropCaps_Book.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DropCaps_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DropCaps_Bold.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DrpoCaps_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DrpoCaps_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DropCaps_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DropCaps_BoldOblique.png'
     i.save()
     closeDoc()
     
     
     ###drop shadow
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DS_Book.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DS_Book.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DS_Bold.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DS_Bold.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DS_Oblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DS_Oblique.png'
     i.save()
     closeDoc()
     
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/DS_BoldOblique.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/DS_BoldOblique.png'
     i.save()
     closeDoc()
     
     ###column intext
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/col_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/col_text.png'
     i.save()
     closeDoc()
     
     ###offset of baseline characters
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Offset_baseline_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Offset_baseline_char.png'
     i.save()
     closeDoc()
     
     ###manual tracking
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Manual_Tracking.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Manual_Tracking.png'
     i.save()
     closeDoc()
     
     ###scaling width of characters
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/scaling_width_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/scaling_width_char.png'
     i.save()
     closeDoc()
     
     ###scaling hight of characters
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/scaling_hight_char.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/scaling_hight_char.png'
     i.save()
     closeDoc()
     
     ###word tracking min
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/word_tracking_min.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/word_tracking_min.png'
     i.save()
     closeDoc()
     
     ###word tracking norm
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/word_tracking_norm.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/word_tracking_norm.png'
     i.save()
     closeDoc()
     
     ###Glyph extension max
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Glyph_extension_max.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Glyph_extension_max.png'
     i.save()
     closeDoc()
     
     ###Glyph extension min
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Glyph_extension_min.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Glyph_extension_min.png'
     i.save()
     closeDoc()
     
     ###OPtical Margins Both Side
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/optical_margins_BothSide.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/optical_margins_BothSide.png'
     i.save()
     closeDoc()
     
     ###OPtical Margins Left Side
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/optical_margins_Left.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/optical_margins_Left.png'
     i.save()
     closeDoc()
     
     ###OPtical Margins Right Side
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/optical_margins_Right.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/optical_margins_Right.png'
     i.save()
     closeDoc()
     
     ###Hyphenation
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Hyphenation.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Hyphenation.png'
     i.save()
     closeDoc()
     
     ###Path text properties
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Path_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Path_text.png'
     i.save()
     closeDoc()
     
     ##Orphans and widows keep next paragraph
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Orphans_Widows_KeepNextParagraph.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Orphans_Widows_KeepNextPar.png'
     i.save()
     closeDoc()
     
     ##Orphans and widows do not split paragraph
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Orphans_Widows_DoNotSplit.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/Orphans_Widows_DoNotSplit.png'
     i.save()
     closeDoc()
     
     ##star Test
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/Star_test.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/star_test.png'
     i.save()
     closeDoc()
     
     ##polygon Test
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/test_polygon.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/polygon.png'
     i.save()
     closeDoc()
     
     ##insert picture in image Frame Test
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/imageFrame.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/imageFrame.png'
     i.save()
     closeDoc()
     
     ##table test
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/table_test.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/table_test.png'
     i.save()
     closeDoc()
     
     ##underLine_word
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/underLine_word.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/underLine_word.png'
     i.save()
     closeDoc()
     
     ##underLine_text
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/underLine_text.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/underLine_text.png'
     i.save()
     closeDoc() 
     
     
     ##all Caps
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/allCaps.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/allCaps.png'
     i.save()
     closeDoc() 
     
     ##small Caps
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/smallCaps.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/smallCaps.png'
     i.save()
     closeDoc() 
     
      ##strike out
     openDoc("/home/u101273/dev/dev/trunk/bin/tests/slas/strikOut.sla")
     i = ImageExport()
     i.type = 'PNG' # select one from i.allTypes list\n\
     i.scale = 100 # I want to have 200%\n\
     i.name = '/home/u101273/dev/dev/trunk/bin/tests/out/strikOut.png'
     i.save()
     closeDoc()
     
if __name__ == '__main__':
    main1()
