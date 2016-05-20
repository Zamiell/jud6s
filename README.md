# The Jud6s Mod v1.23
##### A racing mod for The Binding of Isaac: Afterbirth

<br /><br />

## Download

[Download the latest version here.](https://github.com/Zamiell/jud6s/releases/download/v1.23/jud6s.v1.23.zip)

<br />

## What Is It?

This is a mod that stays very close to the original game while slightly tweaking it to be more fair for racing. It also fixes a ton of bugs that the developers have not bothered to fix in the vanilla game.

This mod is commonly used while racing on [SpeedRunsLive](http://www.speedrunslive.com/races/game/#!/isaacafterbirth/1) and is the mod chosen for most tournaments, such as [Roid Rage](http://roidragetv.weebly.com/) and [Balls of Steel](http://www.ballsofsteel.tv/).

<br />

## Installation & Uninstallation

#### Windows

Double click on the "INSTALL (Windows)" script. It will take care of everything for you. (This script can also be used to uninstall the mod.)

Alternatively, you can manually install the mod by going into the subdirectory that corresponds with the ruleset that you want to play and then copying all of the files to:

`C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\resources\`

To go back to an un-modded game, delete everything in the folder except for the "packed" directory.

#### Mac & Linux

Run the `INSTALL (Mac & Linux).sh` script. It should automatically detect your `resources` folder location. The script will prompt for confirmation before deleting anything.

Alternatively, you can manually install the mod by going into the subdirectory that corresponds with the ruleset that you want to play and then copying all of the files to the `resources` folder.

<br />

## Ruleset

The mod is meant to be played:
* with Judas
* on normal mode
* with the BLCK CNDL seed ("total curse immunity")
* on a "1001%" save file (which is a save file that has everything in the game unlocked)

If don't already have one, you can [download a save file from Speedrun.com](http://www.speedrun.com/saves/fully_unlocked_afterbirth_save_k5imn.zip).

<br />

## Mod Changes

1. Judas is tweaked:
  * Judas starts with the D6. (All other characters also start with the D6, except for Eve, Eden, and Keeper, as it isn't possible.)
  * Judas starts with half a soul heart in addition to his 1 red heart container (so that he can consistently take a devil deal).
  * Judas starts with a bomb instead of 3 coins (so that he can get Treasure Room pedestal items surrounded by rocks).
2. Devil Rooms and Angel Rooms are buffed:
  * Devil Rooms and Angel Rooms without item pedestals in them have been removed.
3. Some items with no effect are removed:
  * the Karma trinket (all Donation Machines are removed on the BLCK CNDL seed)
  * the Amnesia pill (all curses are removed on the BLCK CNDL seed)
  * the ??? pill (all curses are removed on the BLCK CNDL seed)
4. Cutscenes are removed.
5. Some useless animations are removed:
  * cowering in the fetal position at the beginning of every floor
  * jumping in a hole to the next floor
  * going up the beam of light to the Cathedral
  * entering a chest when going to The Chest or beating the game
6. Some death animations are shortened:
  * Boss death animations that are longer than 1 frame are set to 1 frame.
  * The Satan death animation is set to 30 frames.
  * Krampus, Uriel, Gabriel, and It Lives are unchanged.
7. Some bug fixes:
  * Charge animations with transformations now work.
  * Many rooms with unavoidable damage or bugs have been fixed or deleted. Full documentation can be found below.
8. Lag reduction:
  * Fog has been removed to help eliminate lag on slower computers and make the game clearer to see.
  * A [config.ini file](https://steamcommunity.com/app/250900/discussions/0/613941122558099449/) has been included to disable some graphical effects, such as the water on Flooded Caves. It will only be installed if you install the mod with the provided installer script. If you already have a config.ini in your resources directory, then the installer script will not bother copying one over. If you don't like the way that the config.ini makes the game look, simply delete the file from your resources directory or make the contents completely blank.

#### Extra Changes in "Seeded Mode"
* All characters start with The Compass in addition to their other items.
* Angel statues are replaced with either Uriel or Gabriel. Key Piece 1 has been placed in each Angel Room.
* Pandora's Box, Teleport!, Undefined, and Book of Sin are removed from all item pools.
* The Cain's Eye trinket is removed from the game.

#### Extra Changes for "Dark Room Mode"
* 4 golden chests will now spawn at the beginning of the Dark Room (instead of red chests).
* We Need To Go Deeper! is removed from all item pools.
* There are special graphics for The Polaroid, The Negative, and the beam of light that takes you to the Cathedral.

#### Extra Changes for "The Lost Child Open Loser's Bracket Mode"
* The changes from the "Dark Room Mode" are included in this ruleset.
* Judas starts with Judas' Shadow in addition to his other items.
* Judas starts with 0 health.

<br />

## Shoutouts

* [Chronometrics](http://www.twitch.tv/chronometrics) deserves recognition for making and continuing to support [Basement Renovator](https://github.com/Tempus/Basement-Renovator).
* Thanks to all of the racers who have given me feedback, including [Hyphen-ated](http://www.twitch.tv/Hyphen_ated), [Cyber_1](http://www.twitch.tv/Cyber_1), [Ou_J](http://www.twitch.tv/Ou_J), [HauntedQuest](http://www.twitch.tv/HauntedQuest), [Dea1h](http://www.twitch.tv/Dea1h), [Krakenos](http://www.twitch.tv/Krakenos), and [nicoluwu](https://www.twitch.tv/nicoluwu).
* [Dan](https://moddingofisaac.com/user/255) created [the Fogless! mod](https://moddingofisaac.com/mod/950/fogless), which is included in the Jud6s mod.
* [Gromfalloon](http://www.twitch.tv/gromfalloon) originally created the Dark Room graphics.
* [Ipn](https://github.com/lpn) created the Windows installation script.
* [viroulep](https://github.com/viroulep) created the Mac/Linux installation script.

<br />

## Feedback

The changes in this mod are not set in stone. You can discuss the mod with me by contacting me [on Twitch](http://www.twitch.tv/zamiell) or in the [#isaac SpeedRunsLive IRC channel](http://www.speedrunslive.com/channel/).

<br />

## Documentation of Exact Room Changes

The technical details of the mod are listed here for those who truly care to know all of the specifics.

<br />

### Devil Room Buff

* No-item Devil Rooms have been changed to have 1 item. This affects balance in a non-trivial way. Without getting into too much detail, the pros outweigh the cons; a no-item devil deal is disproportionately punishing to a player who has played flawlessly for the entire floor. Furthermore, the overall power increase of a Devil Room becomes more consistent.
* Devil Rooms have been slightly tweaked to have exits on all sides. Otherwise, expected item pedestal amount would change depending on the entrance location.

The changed rooms are as follows:
* #5 (red chests)
* #11 (2 items and 2 Nulls)
* #13 (1 item and Mom's Hand)
* #14 (2 black hearts and 1 Imp)
* #15 (1 item, narrow)

<br />

### Angel Room Buff

Angel Rooms are buffed in a similar manner that Devil Rooms are (for the same reasons). This also has the added benefit of bringing Angel Rooms closer in power to Devil Rooms, making them a viable alternative.

The deleted rooms are as follows:
* #7 (1 eternal heart and 4 soul hearts)
* #4 (2 eternal hearts)
* #3 (3 soul hearts)

<br />

### Dople & Evil Twin Fix

When holding down the tear fire button and entering a room with a Dople or Evil Twin, the player is hit with an unavoidable tear. This bug is fixed by changing all the spawn points of the enemies to be near the corner of the room. Once the room is loaded, the enemy will snap back to where they are supposed to be, but the initial buggy tear will not be in line with the player.

The changed rooms are as follows:
* Womb: #56-#62, #114-#118, #259-#261, #289, #301, #598, #605, #624, #646, #661 
* Utero: #56-#62, #114-#117, #259-#261, #289, #301, #598, #605, #624, #646, #661
* Sheol: #19-#24, #42, #56-#57, #61, #166, #181, #188, #196
* Dark Room: #272

<br />

### Double Boss Champion Fix

Some rooms have Monstros, Gurdy Jr.'s, or Cages that spawn near an entrance. If the double champion version spawns and they happen to spawn in a diagonal orientation, the player will be touched while the room is loading and automatically take damage. This bug is fixed by moving the enemies closer to the center of the room.

The changed rooms are as follows:
* Utero: #133 (Gurdy Jr.)
* Sheol: #212 (Cage)
* Chest: #43, #69 (Monstro)
* Chest: #14, #56 (Gurdy Jr.)
* Chest: #34 (Cage)
* The Dark Room: #14 (Cage)
* The Dark Room: #34 (Monstro)

<br />

### Double Forsaken Fix

If one Forsaken does a Brimstone attack in a clockwise direction and the other Forsaken does a Brimstone attack in a counter-clockwise direction, it is impossible to dodge.

The deleted room is as follows:
* Chest: #296

<br />

### Exploding Enemies Fix

Some rooms have exploding enemies that spawn near an entrance. If the player has a sufficient number of unused blue flies, the flies will kill the enemy while the room is loading and the player will automatically take damage. This bug is fixed by moving the enemy closer to the center of the room.

The changed rooms are as follows:
* Basement: #129, #130, #393, #359 (Mulligan)
* Cellar: #129, #130 (Mulligoon)
* Cellar: #359 (Mulligan)
* Caves: #46, #50, #440, #518 (Boom Fly)
* Caves: #141 (Clotty)
* Caves: #255 (Maggot)
* Caves: #553 (Hive)
* Caves: #548 (Drowned Hive)
* Catacombs: #46, #440, #518 (Boom Fly)
* Catacombs: #548 (Drowned Hive)
* Depths: #11 (Boom Fly)
* Womb/Utero: #203 (Lump)
* Womb: #333 (Fistula)
* Womb: #410 (Sucker)
* Utero #333 (Fistula)
* Utero #410 (Sucker)
* Cathedral: #30 (Kamikaze Leech)
* Cathedral: #272 (Floating Knight)
* Sheol: #30 (Kamikaze Leech)
* Chest: #53, #72, #84 (Fistula)
* Dark Room: #238, #272 (Kamikaze Leech)
* Dark Room: #264 (Bone Knight)

<br />

### TNT Barrel Fix

One Treasure Room has TNT barrels that spawn near the entrance. Upon loading the room, there is a small chance that they will explode. If this occurs, the player will take unavoidable damage. Additionally, a basement/cellar room has TNT barrels that will immediately explode if the player is holding Mom's Knife. These rooms have been fixed by replacing or removing the barrels in question.

The changed room is as follows:

* Treasure Room: #13
* Basement: #748
* Cellar: #748

<br />

### Fly Champion Fix

Certain enemies spawn near a door. If they spawn as the white fly champion version, the player will be touched while the room is loading and automatically take damage. This bug is fixed by moving them closer to the center of the room.

The changed rooms are as follows:
* Cellar: #236 (Sack)
* Womb: #182, #471, #508, #733 (Gurglings)
* Utero: #182, #471, #733 (Gurglings)
* Chest: #35, #87, #301 (Gurglings)

<br />

### Chunky Poop Fix

If a poop that is next to an entrance randomly spawns as a chunky poop, it can lead to unavoidable damage in certain situations. This bug is fixed by moving the poops over by one square.

The changed room is as follows:
* Basement: #124 (4 Gapers and 4 Gushers; also moved Gushers to prevent unavoidable damage on Ipecac)

<br />

### Begotten Fix

If a player enters from the bottom door of the 2x1 Depths / Necropolis room with the single Begotten, they will automatically take damage. It seems clear that Edmund intended for there to only be a top door in room, so the room has been changed in that manner to fix this bug.

The changed rooms are as follows:
* Depths: #316
* Necropolis - #316

<br />

### Clustered Gaping Maws Fix

* If a player with flying and base movement speed gets close to 4 Gaping Maws paired together, it becomes impossible to escape. This was fixed in Womb #424 by adding two Broken Gaping Maws, but the developers forgot to also make the change to Utero #424. I've fixed it for them.
* In both of these rooms, there is no consistent strategy to avoid damage when entering from the bottom-left-hand door. Two pots have been placed to alleviate this.

The changed rooms are as follows:
* Womb: #424
* Utero: #424

<br />

### Adversary Room Removal

While not technically unavoidable, the random nature of the boss movement combined with off-screen Brimstone attacks makes for a very unfair room.

The deleted room is as follows:
* Dark Room: #50 (double Adversary, 2x1)
* Dark Room: #78 (triple Adversary, 2x2)

<br />

### Adversary Fix

If two Adversaries get close to a wall, the Brimstone attack can be unavoidable. This is mitigated by moving the Adversaries closer to the middle of the room.

The changed rooms are as follows:
* Chest: #41
* Dark Room: #7

<br />

### Unfair Narrow Room Removal

While not technically unavoidable, many narrow rooms have near-impossible attack patterns, especially on Dr. Fetus builds.

The deleted rooms are as follows:
* Angel Room: #9
* Boss: #2305 (Krampus)
* Boss: #2306 (Krampus)
* Boss: #4036 (War)
* Boss: #5035 (Mega Maw)
* Boss: #5043 (The Gate)
* Cathedral: #286 (Uriel)
* Cathedral: #291 (Gabriel)
* Chest: #258 (The Haunt) - This room was never play-tested and actually results in soft-lock on most builds.
* Chest: #262 (Headless Horseman Head x2)
* Chest: #269 (Mega Maw)
* Chest: #264, #273 (Monstro x2)
* Chest: #275 (The Fallen)
* Chest: #283 (Gurdy Jr.)
* Chest: #309 (Monstro x4)
* Dark Room: #255, #274 (Teratoma)
* Dark Room: #256, #275 (The Fallen)
* Dark Room: #263 (The Forsaken)
* Dark Room: #270 (4 Nulls)
* Dark Room: #312 (5 Nulls)

<br />

### Narrow Pride Fix

While not guaranteed, certain bomb spawns cause unavoidable damage in combination with the TNT barrels. The barrels have been removed to fix this.

The changed room is as follows:
* #2065

<br />

### Boss Room Door Fix

It is not possible for Devil Room doors to spawn on boss rooms that only have one entrance. For this reason, several rooms were adjusted to allow for two entrances.

The changed rooms are as follows:
* #2065 (Fistula)
* #5026 (Dingle)
* #5145 (Gurglings)
* #5035 (Mega Maw)
* #5044 (The Gate)

<br />

### Blastocyst Fix

In certain rooms with Blastocyst near a door, the player is not given enough time to reasonably dodge the first attack. The Blastocyst are slightly moved to alleviate this. On the boss room, two rocks are also placed to protect the top and bottom entrances.

The changed room is as follows:
* Boss: #2042
* Chest: #54

<br />

### Monstro II & Sucker Fix

When entering from the top or bottom door of the Monstro II boss room with the four Suckers, the player is not given enough time to reasonably dodge the Sucker tear. The Suckers are slightly moved to alleviate this.

The changed room is as follows:
* #1067

<br />

### Carrion Queen Fix

In some rooms, Carrion Queen spawns very close to an entrance. This is fixed by moving her slightly closer to the center of the room.

The changed rooms are as follows:
* #3270
* #3272
* #3273

<br />

### Pin, Frail, and Scolex Fix

On Pin, Frail, and Scolex fights, there is an invisible hitbox during the beginning of the fight. On some rooms, this is near the entrance. This is fixed by moving the spawn to the center of the room.

The changed rooms are as follows:
* #3370 (Pin)
* #3371 (Pin)
* #3372 (Pin)
* #3374 (Pin)
* #3376 (Pin)
* #3388 (Frail)
* #1070 (Scolex)
* #1071 (Scolex)
* #1073 (Scolex)
* #1074 (Scolex)

<br />

### Loki, Lokii, and Death Devil Room Fix

If the player is out of bombs and a Devil Room spawns on the top of the Loki or Loki II room filled with rocks, they will not be able to access it. If the Devil Room spawns on the bottom, the player will be forced to take the boss item in order to see the deal. This is also the case for the Death room filled with pits. This bug is fixed by moving/deleting the rocks/pits respectively.

The changed rooms are as follows:
* #2031 (Loki)
* #3311 (Lokii)
* #4041 (Death)

<br />

### Gurdy Maneuverability Fix

In the Gurdy room filled with pits, the player is forced to take the boss item in order to exit the floor. This bug is fixed by deleting some pits to allow for more maneuverability.

The changed room is as follows:
* #1066 (Gurdy)

<br />

### Turdling Soft-lock Fix

In the Turdling room with pots, sometimes Dips can get inside the pots and the wall, causing a soft-lock. This bug is fixed by changing the pots to poops.

The changed room is as follows:
* #5151 (Turdling)

<br />

### Technology Soft-lock Fix

Certain rooms that require the player to angle their shots can make a Technology build with no bombs soft-lock. The rooms are fixed by replacing some rocks with poops.

The changed rooms are as follows:
* Catacombs: #328
* Depths: #226
* Necropolis: #226

### Low Range Soft-lock Fix

Low range builds soft-lock in certain rooms. The rooms are fixed by moving the enemies closer.

The changed rooms are as follows:
* Caves: #226, #305
* Catacombs: #305
* Depths: #226
* Necropolis: #226
* Womb: #458, #459
* Utero: #458, #459

<br />

### Card Room Fix

The rooms with a bugged Magician / High Priestess card are fixed to be a random card.

The changed rooms are as follows:
* Depths: #286
* Necropolis: #286
* Womb: #687
* Utero: #687
* Dark Room: #291

<br />

### Narrow Red Poop Room Fix

On Dr. Fetus builds, the narrow red poop room in The Chest is unavoidable damage. This bug has been fixed by deleting some of the poops to allow for a walkable path.

The changed room is as follows:
* The Chest: #289

<br />

### Rage Creep & Round Worm Room Fix

One room in the Womb / Utero has two Rage Creeps and four Round Worms in the center. In Afterbirth, the top Rage Creep will hit the player if they stay at the top door. However, this is not unavoidable damage, as it is possible to kill the top Rage Creep before it fires. Alternatively, it is possible to run to the bottom wall before either Rage Creep begins firing. However, the pot in the center of the room messes with the AI of the Round Worms, so the pot has been removed to make traversing this room slightly more consistent.

The changed rooms are as follows:
* Womb: #202
* Utero: #202

<br />

### Troll Bomb Room Removal

For certain rooms with troll bombs, there is no consistent strategy to navigate the room without taking damage.

The removed rooms are as follows:
* Basement: #752, #767
* Cellar: #752, #767
* Depths: #699
* Necropolis: #699
* Sheol: #285

<br />

### Black Bony Fix

In rooms with two Black Bonies placed between pots, they will become stuck on each other. This bug is fixed by spreading them out slightly.

The changed rooms are as follows:
* Depths: #668, #731
* Necropolis: #668, #731

<br />

### Maggot Room Fix

On the room filled with pits in the Caves, at base damage, Maggots are unavoidable if they decide to path towards you. Furthermore, a Dr. Fetus build has no options with which to dodge the first bomb. This is fixed by moving the Maggots slightly towards the center of the room.

The changed room is as follows:
* Caves: #6

<br />

### Leaper & Pokey Room Fix

On the room with the two Leapers and two Pokeys, certain attack patterns can lead to unavoidable damage. The room has been made slightly more spacious to account for this.

The changed room is as follows:
* Depths: #110

<br />

### Pooter Fix

On certain rooms in the Basement/Cellar, some Pooters can fly over rocks, causing a soft-lock.

The deleted room is as follows:
* Basement: #811
* Cellar: #811

The changed rooms are as follows:
* Basement: #135, #391, #534, #747

<br />

### Bomb Puzzle Room Fix

On the bomb puzzle room with four entrances, the random bomb drops were replaced with a set bomb drop to prevent troll bombs from spawning. Also, a rock was also removed to prevent a soft-lock if the player enters from the left side.

The changed room is as follows:
* Depths: #41
* Necropolis: #41

<br />

### Red Fire Puzzle Room Removal

The puzzle rooms with the red fires along the sides of the room have no consistent strategy with which to avoid the random shots.

The removed room is as follows:
* Basement: #771
* Cellar: #771

<br />

### Trapdoor Room

On Sheol, there exists a room with a trapdoor that takes you directly to the Dark Room without having to fight Satan. This puts too much of an extreme lower bound on the clear time of the floor.

The removed room is as follows:
* Sheol: #290

<br />

### Treasure Room Fix for Judas

The Treasure Room with two pedestals and spikes has been slightly tweaked so that Judas can use a bomb to get the item without spending a soul heart.

The changed room is as follows:
* Treasure Room: #21

<br />

### Donation Machine Room Removal

One room in the Necropolis has a donation machine in it. With donation machines removed from the game, this room is largely useless.

The removed room is as follows:
* Necropolis: #469

<br />

### Empty Room Removal

Several rooms in the game are completely empty of any objects at all.

The removed rooms are as follows:
* Basement: #39, #315
* Cellar: #39
* Caves: #170
* Depths: #378, #428
* Sheol: #73, #89, #255
* Cathedral: #57, #89
* Chest: #42

<br />

### Out of Bounds Fix

Rooms with entities out of bounds have been placed in bounds. This does not affect gameplay in any way.

* Caves: #203, #363, #406, #427, #429
* Catacombs: #363, #406, #427, #429
* Depths: #430, #455, #463
* Necropolis: #430, #455

<br />

### Symmetry Fix

Certain rooms in the game were meant to be symmetrical, but one entity or tile was incorrectly placed. This is fixed.

* Basement/Cellar: #772
* Caves: #28, #120, #416
* Womb/Utero: #705

<br />

## Rooms That Were Deliberately Not Changed

* Basement #274 - This is a 1x1 room with a TNT barrel to the left/right of the top/bottom entrances. However, on a knife build, if you are playing correctly, you should be pointing it towards the center of the room upon entering.
* Basement/Cellar #401 - This is a 2x1 room with 4 Pooters. If there is a tinted rock in the room, you should ignore it and hustle to kill the Pooters before they get into a soft-lock position.
* Cellar #766 - This is a 1x1 room with 3 mega troll bombs, but if you stand completely still, they will not damage you.
* Caves #161, #271, #553 - If the enemy by the top door is a explosive champion, the player will not be hit. If the enemy by the top door is a tear champion, the player has a full second to react upon entering.
* Caves #692 - This is a narrow 1x1 room filled with poops. With Ipecac, you can safely shoot left from the top right-hand corner. With Dr. Fetus, you can walk diagonally through the poops to plant your first bomb. With Dr. Fetus and Bomber Boy, it is unavoidable damage.
* Catacombs #267 - This is a room with a Night Crawler right next to the bottom entrance. Night Crawler's cannot spawn as champions, so it will never explode in your face from blue flies.
* Womb/Utero #147 - This is a room with 3 Nerve Endings next to the entrance. If you have Ipecac, it is possible to use a tear on the wall to safely kill a Nerve Ending. Alternatively, you can safely use a bomb.
* Dark Room #287 - This is a room with 3 mega troll bombs and an Imp. If you stand completely still, the troll bombs will not damage you.
* Chest #39 - This is a room with 2 Mega Maws. Even with the champion version, there is enough time to react to the patterns.
* Mama Gurdy - In Afterbirth, you have more time to dodge the spikes before the hitbox appears.
* Daddy Long Legs - In Afterbirth, the multiple stomp attack no longer damages you before the animation begins.
* The Forsaken - Before doing the Brimstone attack, he moves to the center of the room, giving you enough space to dodge, even in a narrow room.

<br />

## Version History

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
