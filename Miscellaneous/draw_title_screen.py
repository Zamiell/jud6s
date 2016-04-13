# Imports
import os
from PIL import Image, ImageFont, ImageDraw

# Configuration
title_screen_text = 'Jud6s Mod v1.21'

# Draw the version number on the title menu graphic
large_font = ImageFont.truetype('IsaacSans.ttf', 19)
title_img = Image.open('titlemenu-base.png')
title_draw = ImageDraw.Draw(title_img)
title_draw.text((345, 247), title_screen_text, (134, 86, 86), font=large_font)
title_img.save('../Ruleset 1 - Normal/gfx/ui/main menu/titlemenu.png')
title_img.save('../Ruleset 2 - Seeded/gfx/ui/main menu/titlemenu.png')
title_img.save('../Ruleset 3 - Dark Room/gfx/ui/main menu/titlemenu.png')
title_img.save('../Ruleset 4 - Seeded Dark Room/gfx/ui/main menu/titlemenu.png')
title_img.save('../Ruleset 5 - LCO Loser\'s Bracket/gfx/ui/main menu/titlemenu.png')

print('Success!')
input("Press enter to continue...")
