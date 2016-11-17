# Version History

* *1.34* - November 17th 
  * Fixed the 2x2 Blind Creep low-range softlock room in the Depths and Necropolis. Thanks to Hikarichan for reporting this.
* *1.33* - October 18th
  * Fixed the bug where Lilith did not start with the D6 properly.
* *1.32* - August 28th
  * The documentation for the mod was moved from the README file (and [the GitHub repository page](https://github.com/Zamiell/jud6s)) to [a new website](http://zamiell.github.io/jud6s/).
  * Added [the GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html) to the project.
  * Changed "EnableColorCorrection" in the default "config.ini" back to 1, since it makes the game look too dark without actually increasing performance. (Thanks to Krakenos for this.)
* *1.31* - August 26th
  * Changed the "EnableColorCorrection" and "EnableFilter" values in the default "config.ini" to 0. (They were mistakenly set to 1.)
* *1.30* - August 20th
  * Fixed an unavoidable damage room in the Depths with a champion Brain.
* *1.29* - August 19th
  * Added the D6 to Eve and Keeper for people who are using custom save files.
* *1.28* - July 26th
  * Deleted the L-shaped room with a Forsaken in The Chest.
* *1.27* - June 27th
  * Basement room #581 was made symmetrical.
* *1.26* - June 2nd
  * Deleted all of the modified rulesets from the standalone Jud6s release; these can now be found in the Isaac Racing Mods package.
  * Fixed an unavoidable damage room in the Chest with 7 Gurglings.
* *1.25* - May 28th
  * Fixed the key pieces on The Chest in the Mega Satan ruleset.
  * Fixed an unavoidable damage Dark Room room with 3 Cages.
* *1.24* - May 24th
  * Added a Mega Satan ruleset that includes both key pieces next to the Mega Satan door.
  * Deleted the Seeded Dark Room ruleset.
  * Fixed a near-unavoidable L-shaped Womb room where a Blastocyst spawned too close to the door.
  * Removed an empty room from the Cathedral.
* *1.23* - May 20th
  * Fixed 3 rooms that soft-locked Technology builds.
  * Fixed 9 rooms that soft-lock low-range builds.
  * Removed 2 empty rooms from Sheol.
  * Removed Book of Sin from the seeded rulesets.
  * Fixed the bug with the Utero turret room with retractable spikes. (I made the Womb version of the symmetrical, but forgot to make the Utero version symmetrical.)
  * Fixed the bug where the It Lives death animation was improperly taken out of the Lost Child Open ruleset.
* *1.22* - April 18th
  * Removed the Basement/Cellar puzzle room with the red fires along the sides, as it is sometimes unavoidable damage.
  * Removed the Karma trinket from the game, since all Donation Machines are removed on the BLCK CNDL seed.
  * Removed the Amnesia and ??? pill from the game, since all curses are removed on the BLCK CNDL seed.
  * Removed the Cain's Eye trinket from the game on the seeded rulesets, since starting with The Compass makes it have no effect.
* *1.21* - April 13th
  * Set the the Satan death animation to 30 frames; note that the 3rd phase of the fight will happen a lot quicker now, so be prepared for the stomps.
  * Set The Lamb death animation to 1 frame.
  * Integrated the "Fogless! v1.1" graphics mod by Dan (https://moddingofisaac.com/mod/950/fogless) into the Jud6s mod. This helps eliminate lag on slower computers and makes the game clearer to see.
  * Integrated a config.ini file (https://steamcommunity.com/app/250900/discussions/0/613941122558099449/) into the Jud6s mod. It will only be installed if you install the mod with the provided installer script. This file tells the game to disable certain graphical effects, such as the water on Flooded Caves. This helps eliminate lag on slower computers and makes the game clearer to see. If you already have a config.ini in your resources directory, then the installer script will not bother copying anything over. If you don't like the way that the config.ini makes the game look, simply delete the file from your resources directory.
* *1.20* - April 11th
  * Removed the More Options mode, since nobody uses it anymore.
  * Reverted the skull change in the Depths/Necropolis bomb puzzle room, as it doesn't actually stop spikes from spawning on Dank Depths. If you get spikes spawning on a critical path and you don't have flying, you are pretty much screwed.
  * Fixed a soft-lock in one of the Turdling boss rooms.
  * Fixed an unavoidable damage room with explosive champion Lumps in the Womb.
  * Deleted the trapdoor room on Sheol.
  * Deleted an unavoidable damage room on Sheol with Megatroll Bombs.
  * Deleted an unavoidable damage room on the Dark Room with 4 Nulls.
  * Deleted an unavoidable damage room on the Dark Room with 5 Nulls.
  * Fixed an unavoidable damage room with explosive champion Bone Knights in the Dark Room.
  * Fixed an unavoidable damage room with chunky poop in the Basement. (The Gushers in the room were also moved to address unavoidable damage on Ipecac builds.)
* *1.19* - March 9th
  * Fixed an unavoidable damage room with double Gurdy in Utero.
  * Fixed a soft-lock that occurs in the Womb/Utero room with 4 turrets and very large tears.
* *1.18* - February 22nd
  * Reverted the death animation removal for It Lives, which fixes the bug with the death tears.
  * Fixed an unavoidable damage room with a Mulligan in the Basement.
  * Fixed an unavoidable damage room with a Maggot in the Caves.
  * Removed the useless room with the donation machine in Necropolis.
  * Made Womb/Utero room #705 and Caves room #28 symmetrical.
* *1.17* - February 9th
  * Fixed the bug where shields would not show if the player was using the Pony or the White Pony.
  * Changed The Lost Child Open loser's bracket ruleset:
    * The previous changes have been reverted.
    * Judas now starts with Judas' Shadow and 0 HP.
* *1.16* - February 8th
  * Removed the 2x1 Adversary room in the Dark Room.
  * Fixed the Black Bonies on Depths/Necropolis room #668.
* *1.15* - February 7th
  * The installer script will no longer delete config.ini.
  * Reorganized the ruleset numbers.
  * Fixed the door on Basement/Cellar room #772.
  * Fixed the bug where the Pony and the White Pony do not show if the player has certain transformations.
  * Added a new ruleset for The Lost Child Open loser's bracket:
    * Blue Baby now starts with a bomb and an extra half soul heart.
    * Judas Shadow and Lazarus' Rags are removed from all pools.
* *1.14* - January 24th
  * Teleport! and Undefined have been removed from all pools in the seeded mode.
* *1.13* - January 21st
  * The Windows installation script will now attempt to automatically find your "resources" directory using Steam, which means it will now work if you have Isaac installed in a non-standard place. (Thanks to Ipn for this.)
  * Fixed a 2x1 Chest room by moving the Blastocysts slightly away from the doors.
* *1.12* - January 16th 
  * Deleted a Basement/Cellar L-shaped Pooter room.
  * Changed some Basement rooms to fix the Pooter soft-lock.
* *1.11* - January 15th
  * Deleted the Chest narrow double Headless Horseman room.
  * Deleted the Chest narrow Mega Maw room.
  * Deleted the Chest narrow Gurdy Jr. room.
  * Deleted the Chest double Monstro rooms.
  * Deleted the Chest quad Monstro room.
  * Fixed the Cathedral narrow Floating Knight room.
  * Fixed the Womb/Utero 2x2 room with Suckers in the corners.
  * Moved some Adversaries to be closer to the middle of the room.
  * Changed the Polaroid and Cathedral beam graphics to be more obnoxious on the Dark Room mode. (Thanks to Gromfalloon for creating some of the images.)
* *1.10* - January 11th, 2016
  * Added RatRacing's start room graphic.
  * Changed the text on the character select screen for Judas.
  * Added graphics to help from players accidentally taking the Polaroid or going to the Cathedral on the Dark Room mode.
* *1.9* - January 11th, 2016
  * Fixed the Gate boss room with no side entrances.
  * Deleted the narrow Mega Maw room.
* *1.8* - January 10th, 2016
  * Made the installation script better; just edit line 4 if you don't have Afterbirth installed in the normal location.
  * Added a separate installation script for Mac/Linux. (Thanks to viroulep for this.)
  * Deleted the double troll bomb room in the Basement/Cellar.
  * Deleted the narrow Fallen rooms on The Chest / Dark Room.
  * Deleted the Triple Adversary room in the Dark Room.
  * Deleted the narrow Forsaken room on the Dark Room.
  * Deleted the narrow Teratoma rooms on the Dark Room.
  * Fixed a Kamikaze Leech room in the Dark Room.
  * Fixed the High Priestess card room in the Dark Room.
* *1.7* - January 7th, 2016
  * Added a helpful installer script and a shortcut to the Afterbirth resources directory.
  * Added Uriel or Gabriel to every Angel Room on seeded mode.
  * Deleted the double Forsaken room in the Chest.
  * Changed the room in the Depths with the two Leapers and two Pokeys to be more reasonable.
  * Fixed the bomb puzzle room in the Depths/Necropolis.
  * Fixed the room in the Caves with the Hive that was spawning too close to the top entrance.
  * Made a Hive room in the Caves symmetrical.
* *1.6* - January 6th, 2016
  * Reverted the "room variety" change.
  * Fixed the L-shaped room with the Pooters in the Basement/Cellar.
* *1.5* - January 6th, 2016
  * Added a More Options mode.
  * Reverted the "giantbook" animation removal (black heart, Betrayal, and so forth).
  * Changed the Treasure Room with two pedestals and spikes.
  * Reverted the changes to The Haunt room and Mega Fatty room with TNT barrels.
* *1.4* - January 5th, 2016
  * Fixed a bug with certain rooms incorrectly being set to 1000 weight.
* *1.3* - January 5th, 2016
  * Updated the mod for Afterbirth and added some other goodies.
  * Moved the documentation from the Medium blog to GitHub.
* *1.2* - July 13th, 2105
  * Added half a soul heart to Judas.
  * Made modifications to some buggy rooms.
* *1.1* - July 1st, 2015
  * The initial public release. The first Balls of Steel weekly was played on this version.
