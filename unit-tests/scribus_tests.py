from PIL import Image,ImageMath
import unittest
import subprocess
import os
import glob

def convert_to_comparable(a, b):
    new_a, new_b = a, b
    if a.mode == 'P':
        new_a = Image.new('L', a.size)
        new_b = Image.new('L', b.size)
        new_a.putdata(a.getdata())
        new_b.putdata(b.getdata())
    elif a.mode == 'I;16':
        new_a = a.convert('I')
        new_b = b.convert('I')
    return new_a, new_b

class ScribusTestCase(unittest.TestCase):
            
    def assert_image_equal(self, a, b, msg=None):
        self.assertEqual(
            a.mode, b.mode,
            msg or "got mode %r, expected %r" % (a.mode, b.mode))
        self.assertEqual(
            a.size, b.size,
            msg or "got size %r, expected %r" % (a.size, b.size))
        if a.tobytes() != b.tobytes():
            self.fail(msg or "got different content")
    
    def assert_image (self, image_name):
        img1 = Image.open('images/'+image_name)
        img2 = Image.open('out/'+ image_name)
        self.assert_image_equal(img1, img2)

         
class TestScribusFrame(ScribusTestCase):

          ##LEFT TO RIGHT testing
         def test_text_LTR_left(self):
           self.assert_image('LTR_left.png')
           
         def test_text_LTR_center(self):
           self.assert_image('LTR_center.png')
            
         def test_text_LTR_right(self):
          self.assert_image('LTR_center.png')   
            
         def test_text_LTR_justified(self):
           self.assert_image('LTR_justifid.png')
        
         def test_text_LTR_Forcedjustified(self):
          self.assert_image('LTR_Forcedjustified.png')
       
         ####RIGHT TO LEFT testing
         def test_text_RTL_left(self):
          self.assert_image('RTL_left.png')
           
         def test_text_RTL_center(self):
           self.assert_image('RTL_center.png')
           
         def test_text_RTL_right(self):
           self.assert_image('RTL_right.png')
           
         def test_text_RTL_justified(self):
           self.assert_image('RTL_justified.png')
           
         def test_text_RTL_FOrcedjustified(self):
           self.assert_image('RTL_forcedjustified.png')
           
         ##################################Font testing
         ###Fixed linespacing
         def test_font_FixedLI_Book(self):
           self.assert_image('FixedLI_Book.png')
           
         def test_font_FixedLI_Bold(self):
           self.assert_image('FixedLI_Bold.png')
          
         def test_font_FixedLI_BoldOblique(self):
           self.assert_image('FixedLI_BoldOblique.png')
           
         def test_font_FixedLI_Oblique(self):
           self.assert_image('FixedLI_Oblique.png')
        
           ####Auto linespacing
         def test_font_Auto_Book(self):
           self.assert_image('Auto_Book.png')
           
         def test_font_Auto_Bold(self):
           self.assert_image('Auto_Bold.png')
          
         def test_font_Auto_BoldOblique(self):
           self.assert_image('Auto_BoldOblique.png')
           
         def test_font_Auto_Oblique(self):
           self.assert_image('Auto_Oblique.png')
           
           #######colerd text test
         def test_color_GreenCol_Bold(self):
           self.assert_image('GreenCol_Bold.png')
           
         def test_color_RedCol_Book(self):
           self.assert_image('RedCol_Book.png')
           
         def test_color_BlueCol_BoldOblique(self):
           self.assert_image('BuleCol_BoldOblique.png')
           
         def test_color_yellowCol_Oblique(self):
           self.assert_image('yellowCol_Oblique.png')
           
           #######fill textbox
         def test_color_FillGreen_Book(self):  
           self.assert_image('FillGreen_Book.png')
           
         def test_color_FillMagenta_Bold(self):
           self.assert_image('FillMagenta_Bold.png')
           
         def test_color_FillBlue_Oblique(self):
           self.assert_image('FillBlue_Oblique.png')
           
         def test_color_FillYellow_BoldOblique(self):
           self.assert_image('FillYellow_BoldOblique.png')
    
          ###Drop Caps
          
         def test_DropCaps_Bold(self):  
           self.assert_image('DropCaps_Bold.png')
           
         def test_DropCaps_BoldOblique(self):
           self.assert_image('DropCaps_BoldOblique.png')
          
         def test_DropCaps_Book(self):
           self.assert_image('DropCaps_Book.png')
          
         def test_DrpoCaps_Oblique(self):
           self.assert_image('DrpoCaps_Oblique.png')
          
           ###Drop Shadow
         def test_DS_Bold(self):  
           self.assert_image('DS_Bold.png')
           
         def test_DS_BoldOblique(self):
           self.assert_image('DS_BoldOblique.png')
           
         def test_DS_Book(self):
           self.assert_image('DS_Book.png')
            
         def test_DS_Obliquee(self):
           self.assert_image('DS_Oblique.png')
           
           ###2 column text test
         def test_col_text(self):
           self.assert_image('col_text.png')
          
         ###offset of baseline characters
         def test_Offset_baseline_charc(self):
           self.assert_image('Offset_baseline_char.png')
           
           ##Manual_Tracking
         def test_Manual_Tracking(self):
           self.assert_image('Manual_Tracking.png')
           
            ###scaling hight of characters
         def test_scaling_hight_char(self):
          self.assert_image('scaling_hight_char.png')
           
            ###scaling width of characters
         def test_scaling_width_char(self):  
           self.assert_image('scaling_width_char.png')
           
           ###word tracking min
         def test_word_tracking_min(self):
           self.assert_image('word_tracking_min.png')
           
           ###word tracking norm
         def test_word_tracking_norm(self):
           self.assert_image('word_tracking_norm.png')
           
           ###Glyph_Extension_min
         def test_Glyph_extension_min(self):
           self.assert_image('Glyph_extension_min.png')
           
           ###Glyph_Extension_max
         def test_Glyph_extension_max(self):
           self.assert_image('Glyph_extension_max.png')
           
           ###OPtical Margins Both Side
         def test_optical_margins_BothSide(self):
           self.assert_image('optical_margins_BothSide.png')
           
           ###OPtical Margins Left Side
         def test_optical_margins_Left(self):
           self.assert_image('optical_margins_Left.png')
           
           ###OPtical Margins Right Side
         def test_optical_margins_Right(self):
           self.assert_image('optical_margins_Right.png')
           
           ###Hyphenation
         def test_Hyphenation(self):
           self.assert_image('Hyphenation.png')
           
           ###Path text properties
         def test_Path_text(self):
           self.assert_image('Path_text.png')
           
           ##Orphans and widows do not split paragraph
         def test_Orphans_Widows_DoNotSplit(self):
           self.assert_image('Orphans_Widows_DoNotSplit.png')
           
          ##Orphans and widows keep next paragraph
         def test_Orphans_Widows_KeepNextPar(self):
           self.assert_image('Orphans_Widows_KeepNextPar.png')
           
           ###star_test
         def test_star(self):
           self.assert_image('star_test.png')
           
           ###test polygon Test
         def test_Polygon(self):
           self.assert_image('polygon.png') 
           
           ###insert picture in image Frame Test
         def test_insert_pic_imageFrame(self):
           self.assert_image('imageFrame.png') 
           
           ##table test
         def test_table(self):
           self.assert_image('table_test.png') 
           
           ##underLine_word
         def test_underLine_word(self):
           self.assert_image('underLine_word.png') 
           
           ##underLine_word
         def test_underLine_text(self):
           self.assert_image('underLine_text.png')  
           
           #all caps
         def test_allCaps(self):
           self.assert_image('allCaps.png')
           
            #small caps
         def test_smallCaps(self):
           self.assert_image('smallCaps.png')
           
           #strik out
         def test_strikOut(self):
           self.assert_image('strikOut.png')
     
if __name__ == '__main__':
    subprocess.call(["../scribus", "-ns", "-g", "-py","export_imgs.py"])
    unittest.main()
