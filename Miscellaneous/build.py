#! C:\Python35\python.exe

# Imports
import os
import shutil
import zipfile
from PIL import Image, ImageFont, ImageDraw

# Configuration
version = '1.25'
title_screen_text = 'Jud6s Mod v' + version
ruleset1 = 'Ruleset 1 - Normal'
ruleset2 = 'Ruleset 2 - Seeded'
ruleset3 = 'Ruleset 3 - Dark Room'
ruleset4 = 'Ruleset 4 - LCO Loser\'s Bracket'
ruleset5 = 'Ruleset 5 - Mega Satan'

# Make a "jud6s_version.txt" file in each of the ruleset directories
with open('../' + ruleset1 + '/jud6s_version.txt', 'w') as f:
    f.write(version)
with open('../' + ruleset2 + '/jud6s_version.txt', 'w') as f:
    f.write(version)
with open('../' + ruleset3 + '/jud6s_version.txt', 'w') as f:
    f.write(version)
with open('../' + ruleset4 + '/jud6s_version.txt', 'w') as f:
    f.write(version)
with open('../' + ruleset5 + '/jud6s_version.txt', 'w') as f:
    f.write(version)

# Draw the version number on the title menu graphic x5
print('Drawing "' + title_screen_text + '" on the title screens...')
large_font = ImageFont.truetype('IsaacSans.ttf', 19)
small_font = ImageFont.truetype('IsaacSans.ttf', 15)

# No ruleset
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_img.save('titlemenu-noruleset.png')

# Ruleset 1
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_draw.text((345, 256), ruleset1, (134, 86, 86), font=small_font)
title_img.save('../' + ruleset1 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset1.png')

# Ruleset 2
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_draw.text((342, 256), ruleset2, (134, 86, 86), font=small_font)
title_img.save('../' + ruleset2 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset2.png')

# Ruleset 3
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_draw.text((333, 256), ruleset3, (134, 86, 86), font=small_font)
title_img.save('../' + ruleset3 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset3.png')

# Ruleset 4
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_draw.text((342, 256), 'LCO Loser\'s Bracket', (134, 86, 86), font=small_font)
title_img.save('../' + ruleset4 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset4.png')

# Ruleset 5
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 239), title_screen_text, (134, 86, 86), font=large_font)
title_draw.text((322, 256), ruleset5, (134, 86, 86), font=small_font)
title_img.save('../' + ruleset5 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('titlemenu-ruleset5.png')

# Copy the rooms files from ruleset 1
print('Copying the rooms files...')
for file_name in os.listdir('../' + ruleset1 + '/rooms'):
    file_full_path = os.path.join('../' + ruleset1 + '/rooms', file_name)

    if (file_name != '00.special rooms.stb'): # Don't copy the special rooms because of the Angel Room change
        shutil.copyfile(file_full_path, '../' + ruleset2 + '/rooms/' + file_name)
    shutil.copyfile(file_full_path, '../' + ruleset3 + '/rooms/' + file_name)
    shutil.copyfile(file_full_path, '../' + ruleset4 + '/rooms/' + file_name)
    if (file_name != '16.dark room.stb' and file_name != '17.chest.stb'): # Don't copy The Chest or Dark Room because of the key pieces change
        shutil.copyfile(file_full_path, '../' + ruleset5 + '/rooms/' + file_name)

# Special rooms must be manually updated in ruleset 2
pass

# The Chest and Dark Room must be manually updated in ruleset 5
pass

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
