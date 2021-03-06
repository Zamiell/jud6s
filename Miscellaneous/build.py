#! C:\Python34\python.exe

# Imports
import os
import sys
import shutil
import zipfile
from PIL import Image, ImageFont, ImageDraw

# Configuration
version = '4.0.10'
title_screen_text = 'Jud6s Mod v' + version

# Make a "jud6s_version.txt" file
with open('../resources/jud6s_version.txt', 'w') as f:
    f.write(version)

# Draw the version number on the title menu graphic
print('Drawing "' + title_screen_text + '" on the title screens...')
large_font = ImageFont.truetype('IsaacSans.ttf', 19)
small_font = ImageFont.truetype('IsaacSans.ttf', 15)

# No ruleset
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
w, h = title_draw.textsize(title_screen_text, font=large_font)
title_draw.text((405 - w / 2, 239), title_screen_text, (134, 86, 86), font=large_font)
#title_img.save('titlemenu-noruleset.png')

# Ruleset 1
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
w, h = title_draw.textsize(title_screen_text, font=large_font)
title_draw.text((405 - w / 2, 239), title_screen_text, (134, 86, 86), font=large_font)
ruleset_name = 'Ruleset 1 - Unseeded'
w, h = title_draw.textsize(ruleset_name, font=small_font)
title_draw.text((405 - w / 2, 256), ruleset_name, (134, 86, 86), font=small_font)
title_img.save('../resources/gfx/ui/main menu/titlemenu.png')
#title_img.save('titlemenu-ruleset1.png')
title_img.save('C:/Users/james/Documents/My Games/Binding of Isaac Afterbirth+ Mods/Jud6s/resources/gfx/ui/main menu/titlemenu.png')

# Make the zip file
sys.exit(0) # We don't want to do this yet for Afterbirth+
print('Making a zip file...')
if os.path.isdir('zipdir'):
    shutil.rmtree('zipdir')
os.makedirs('zipdir')
shutil.copyfile('../README.md', 'zipdir/README.txt')
shutil.copyfile('../INSTALL (Windows).bat', 'zipdir/INSTALL (Windows).bat')
shutil.copyfile('../Shortcut to BoIA Resources Folder.lnk', 'zipdir/Shortcut to BoIA Resources Folder.lnk')
os.makedirs('zipdir/miscellaneous')
shutil.copyfile('config.ini', 'zipdir/miscellaneous/config.ini')
shutil.copytree('../resources', 'zipdir/resources')
shutil.make_archive('../../jud6s-v' + version, 'zip', 'zipdir')
shutil.rmtree('zipdir')

# Done
print('Success!')
input('Press enter to continue...')
