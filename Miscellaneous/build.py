#! C:\Python34\python.exe

# Imports
import os
import shutil
import zipfile
from PIL import Image, ImageFont, ImageDraw

# Configuration
version = '1.26'
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
title_img.save('titlemenu-noruleset.png')

# Ruleset 1
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
w, h = title_draw.textsize(title_screen_text, font=large_font)
title_draw.text((405 - w / 2, 239), title_screen_text, (134, 86, 86), font=large_font)
ruleset_name = 'Ruleset 1 - Unseeded'
w, h = title_draw.textsize(ruleset_name, font=small_font)
title_draw.text((405 - w / 2, 256), ruleset_name, (134, 86, 86), font=small_font)
title_img.save('../resources/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset1.png')

# Rename README.md to README.txt extension so that noobs are less confused
shutil.move('../README.md', '../README.txt')

# Make the zip file
print('Making a zip file...')
shutil.make_archive('../../jud6s-v' + version, 'zip', '..')

# Remove the .git directory from the zip file
zip_in = zipfile.ZipFile ('../../jud6s-v' + version + '.zip', 'r')
zip_out = zipfile.ZipFile ('../../jud6s-v' + version + '.zip2', 'w')
for item in zip_in.infolist():
    buffer = zip_in.read(item.filename)
    if ('.git' not in item.filename):
        zip_out.writestr(item, buffer)
zip_in.close()
zip_out.close()
shutil.move('../../jud6s-v' + version + '.zip2', '../../jud6s-v' + version + '.zip')

# Rename README.txt back to the way it was
shutil.move('../README.txt', '../README.md')

# Done
print('Success!')
input('Press enter to continue...')
