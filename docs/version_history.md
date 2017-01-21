# Version History

* *4.0.5* - January 21st, 2017
  * Changed the new Devil Rooms and Angel Rooms to 1.0 weight (the same as all of the other rooms).
  * Fixed the Boss Rush door not properly opening. (It was related to the WotL-style room clear.)
* *4.0.4* - January 19th, 2017
  * Fixed active item charges not accumulating properly.
* *4.0.3* - January 19th, 2017
  * Chronometrics figured out a way via Lua code to emulate Wrath of the Lamb room clear style (doors opening on the beginning of the death animation instead of the end). Subsequently, all boss death animations have been reverted back to their vanilla length. A huge thanks goes to him! This is now the biggest feature of the Jud6s mod.
  * Chronometrics also figured out a way to stop all of the Void Portals from spawning. No more run ending portals!
  * Note that when using the Jud6s mod, certain characters items will appear buggy in the [Rebirth Item Tracker](https://github.com/Hyphen-ated/RebirthItemTracker/releases) unless you have the latest version of the tracker (v1.2.3 or later).
  * Jud6s still does not contain all of the room fixes. I'll do that later.
* *4.0.2* - January 15th, 2017
  * Azazel now starts with the same health that Judas does. (This is a better solution than giving him an extra half black heart or half soul heart.)
* *4.0.1* - January 15th, 2017
  * Keeper starts with the D6, Greed's Gullet, Duality, and 25 cents. This should make racing him more consistent.
* *4.0.0* - January 14th, 2017
  * Updated the mod for Afterbirth+. I was hoping to do some simple things, like automatically remove curses so that you don't have to type in BLCK CNDL every time. However, the Lua API is extremely limited, so this is impossible (at the current time).
  * You can install the mod by following the instructions on [the Steam workshop page for the mod](http://steamcommunity.com/workshop/filedetails/?id=842735484).
  * The version number is changed to be in the [Semantic Versioning 2.0.0](http://semver.org/) format. It is also bumped up to 4.0.0 so that it will be in-line with the Isaac Racing Mods (which is currently unreleased).
  * There is no unavoidable room changes yet. However, Devil/Angel rooms are fixed, along with the starting room of the Dark Room.
  * Eve and Eden now always start with the D6 (thanks to some new Afterbirth+ hacks).
  * Apollyon now starts with the D6.
  * Judas now starts with a half filled red heart container. (This was the way it was originally intended to be, but was impossible to do until now.)
  * Blue Baby now starts with 3 and a half soul hearts. (This is from [community consensus](http://www.speedrun.com/afterbirth/thread/p82nh).)
  * The "No Achievements" icon has been replaced by Judas' fez to signify that you are playing on the Jud6s mod.
  * The mod no longer includes a "config.ini", since that can't be bundled with a mod. If you want to use a "config.ini" file, just keep one in your resources directory.
  * Afterbirth+ fixed charge animations with Azazel/transformations, so the Jud6s mod no longer includes fixes for that.
  * Removed the "Teleport up" animation, which is fairly useless. (It plays when using a Hermit card, and so forth.)
  * Lengthened all shortened death animations from 1 frame to 4 frames.
* *1.36* - November 18th, 2016
  * Set shields to the highest priority, which should fix the issue with Azazel from the last patch.
* *1.35* - November 18th, 2016
  * Fixed the bug with Azazel where his charge animation was overwritten by Monstro's Lung, Leviathan, and so forth. (This bug is also present in vanilla.) Thanks to Cyber_1 for reporting this.
* *1.34* - November 17th, 2016
  * Fixed the 2x2 Blind Creep low-range softlock room in the Depths and Necropolis. Thanks to Hikarichan for reporting this.
* *1.33* - October 18th, 2016
  * Fixed the bug where Lilith did not start with the D6 properly.
* *1.32* - August 28th, 2016
  * The documentation for the mod was moved from the README file (and [the GitHub repository page](https://github.com/Zamiell/jud6s)) to [a new website](http://zamiell.github.io/jud6s/).
  * Added [the GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html) to the project.
  * Changed "EnableColorCorrection" in the default "config.ini" back to 1, since it makes the game look too dark without actually increasing performance. (Thanks to Krakenos for this.)
* *1.31* - August 26th, 2016
  * Changed the "EnableColorCorrection" and "EnableFilter" values in the default "config.ini" to 0. (They were mistakenly set to 1.)
* *1.30* - August 20th, 2016
  * Fixed an unavoidable damage room in the Depths with a champion Brain.
* *1.29* - August 19th, 2016
  * Added the D6 to Eve and Keeper for people who are using custom save files.
* *1.28* - July 26th, 2016
  * Deleted the L-shaped room with a Forsaken in The Chest.
* *1.27* - June 27th, 2016
  * Basement room #581 was made symmetrical.
* *1.26* - June 2nd, 2016
  * Deleted all of the modified rulesets from the standalone Jud6s release; these can now be found in the Isaac Racing Mods package.
  * Fixed an unavoidable damage room in the Chest with 7 Gurglings.
* *1.25* - May 28th, 2016
  * Fixed the key pieces on The Chest in the Mega Satan ruleset.
  * Fixed an unavoidable damage Dark Room room with 3 Cages.
* *1.24* - May 24th, 2016
  * Added a Mega Satan ruleset that includes both key pieces next to the Mega Satan door.
  * Deleted the Seeded Dark Room ruleset.
  * Fixed a near-unavoidable L-shaped Womb room where a Blastocyst spawned too close to the door.
  * Removed an empty room from the Cathedral.
* *1.23* - May 20th, 2016
  * Fixed 3 rooms that soft-locked Technology builds.
  * Fixed 9 rooms that soft-lock low-range builds.
  * Removed 2 empty rooms from Sheol.
  * Removed Book of Sin from the seeded rulesets.
  * Fixed the bug with the Utero turret room with retractable spikes. (I made the Womb version of the symmetrical, but forgot to make the Utero version symmetrical.)
  * Fixed the bug where the It Lives death animation was improperly taken out of the Lost Child Open ruleset.
* *1.22* - April 18th, 2016
  * Removed the Basement/Cellar puzzle room with the red fires along the sides, as it is sometimes unavoidable damage.
  * Removed the Karma trinket from the game, since all Donation Machines are removed on the BLCK CNDL seed.
  * Removed the Amnesia and ??? pill from the game, since all curses are removed on the BLCK CNDL seed.
  * Removed the Cain's Eye trinket from the game on the seeded rulesets, since starting with The Compass makes it have no effect.
* *1.21* - April 13th, 2016
  * Set the the Satan death animation to 30 frames; note that the 3rd phase of the fight will happen a lot quicker now, so be prepared for the stomps.
  * Set The Lamb death animation to 1 frame.
  * Integrated the "Fogless! v1.1" graphics mod by Dan (https://moddingofisaac.com/mod/950/fogless) into the Jud6s mod. This helps eliminate lag on slower computers and makes the game clearer to see.
  * Integrated a config.ini file (https://steamcommunity.com/app/250900/discussions/0/613941122558099449/) into the Jud6s mod. It will only be installed if you install the mod with the provided installer script. This file tells the game to disable certain graphical effects, such as the water on Flooded Caves. This helps eliminate lag on slower computers and makes the game clearer to see. If you already have a config.ini in your resources directory, then the installer script will not bother copying anything over. If you don't like the way that the config.ini makes the game look, simply delete the file from your resources directory.
* *1.20* - April 11th, 2016
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
* *1.19* - March 9th, 2016
  * Fixed an unavoidable damage room with double Gurdy in Utero.
  * Fixed a soft-lock that occurs in the Womb/Utero room with 4 turrets and very large tears.
* *1.18* - February 22nd, 2016
  * Reverted the death animation removal for It Lives, which fixes the bug with the death tears.
  * Fixed an unavoidable damage room with a Mulligan in the Basement.
  * Fixed an unavoidable damage room with a Maggot in the Caves.
  * Removed the useless room with the donation machine in Necropolis.
  * Made Womb/Utero room #705 and Caves room #28 symmetrical.
* *1.17* - February 9th, 2016
  * Fixed the bug where shields would not show if the player was using the Pony or the White Pony.
  * Changed The Lost Child Open loser's bracket ruleset:
    * The previous changes have been reverted.
    * Judas now starts with Judas' Shadow and 0 HP.
* *1.16* - February 8th, 2016
  * Removed the 2x1 Adversary room in the Dark Room.
  * Fixed the Black Bonies on Depths/Necropolis room #668.
* *1.15* - February 7th, 2016
  * The installer script will no longer delete config.ini.
  * Reorganized the ruleset numbers.
  * Fixed the door on Basement/Cellar room #772.
  * Fixed the bug where the Pony and the White Pony do not show if the player has certain transformations.
  * Added a new ruleset for The Lost Child Open loser's bracket:
    * Blue Baby now starts with a bomb and an extra half soul heart.
    * Judas Shadow and Lazarus' Rags are removed from all pools.
* *1.14* - January 24th, 2016
  * Teleport! and Undefined have been removed from all pools in the seeded mode.
* *1.13* - January 21st, 2016
  * The Windows installation script will now attempt to automatically find your "resources" directory using Steam, which means it will now work if you have Isaac installed in a non-standard place. (Thanks to Ipn for this.)
  * Fixed a 2x1 Chest room by moving the Blastocysts slightly away from the doors.
* *1.12* - January 16th, 2016
  * Deleted a Basement/Cellar L-shaped Pooter room.
  * Changed some Basement rooms to fix the Pooter soft-lock.
* *1.11* - January 15th, 2016
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
