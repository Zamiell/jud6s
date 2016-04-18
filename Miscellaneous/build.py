#! C:\Python34\python.exe

# Imports
import os
import shutil
import zipfile
from PIL import Image, ImageFont, ImageDraw

# Configuration
version = 'v1.22'
title_screen_text = 'Jud6s Mod ' + version
ruleset1 = 'Ruleset 1 - Normal'
ruleset2 = 'Ruleset 2 - Seeded'
ruleset3 = 'Ruleset 3 - Dark Room'
ruleset4 = 'Ruleset 4 - Seeded Dark Room'
ruleset5 = 'Ruleset 5 - LCO Loser\'s Bracket'

# Draw the version number on the title menu graphic
print('Drawing "' + title_screen_text + '" on the title screens...')
large_font = ImageFont.truetype('IsaacSans.ttf', 19)
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 247), title_screen_text, (134, 86, 86), font=large_font)
title_img.save('../' + ruleset1 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('../' + ruleset2 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('../' + ruleset3 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('../' + ruleset4 + '/gfx/ui/main menu/titlemenu.png')
title_img.save('../' + ruleset5 + '/gfx/ui/main menu/titlemenu.png')

# Copy the rooms files from ruleset 1 (but not the special rooms because of the Angel Room change)
print('Copying the rooms files...')
for file_name in os.listdir('../' + ruleset1 + '/rooms'):
    if (file_name == '00.special rooms.stb'):
        continue
    file_full_path = os.path.join('../' + ruleset1 + '/rooms', file_name)

    shutil.copyfile(file_full_path, '../' + ruleset2 + '/rooms/' + file_name)
    shutil.copyfile(file_full_path, '../' + ruleset3 + '/rooms/' + file_name)
    shutil.copyfile(file_full_path, '../' + ruleset4 + '/rooms/' + file_name)
    shutil.copyfile(file_full_path, '../' + ruleset5 + '/rooms/' + file_name)

# Copy the "00.special rooms.stb" file from ruleset 1 to the non-seeded rulesets
shutil.copyfile('../' + ruleset1 + '/rooms/00.special rooms.stb', '../' + ruleset3 + '/rooms/00.special rooms.stb')
shutil.copyfile('../' + ruleset1 + '/rooms/00.special rooms.stb', '../' + ruleset5 + '/rooms/00.special rooms.stb')

# Copy the "00.special rooms.stb" file from ruleset 2 to the seeded rulesets
shutil.copyfile('../' + ruleset2 + '/rooms/00.special rooms.stb', '../' + ruleset4 + '/rooms/00.special rooms.stb')

# Rename README.md to README.txt extension so that noobs are less confused
shutil.move('../README.md', '../README.txt')

# Make the zip file
print('Making a zip file...')
shutil.make_archive('../../jud6s ' + version, 'zip', '..')

# Remove the .git directory from the zip file
zip_in = zipfile.ZipFile ('../../jud6s ' + version + '.zip', 'r')
zip_out = zipfile.ZipFile ('../../jud6s ' + version + '.zip2', 'w')
for item in zip_in.infolist():
    buffer = zip_in.read(item.filename)
    if ('.git' not in item.filename):
        zip_out.writestr(item, buffer)
zip_in.close()
zip_out.close()
shutil.move('../../jud6s ' + version + '.zip2', '../../jud6s ' + version + '.zip')

# Rename README.txt back to the way it was
shutil.move('../README.txt', '../README.md')

# Done
print('Success!')
input('Press enter to continue...').strip()
