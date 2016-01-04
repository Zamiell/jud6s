## Download

[Download the latest version here.](https://github.com/Zamiell/jud6s/releases)



## What is it?

This is a racing mod for *The Binding of Isaac: Afterbirth* that stays very close to the original game while slightly tweaking it to be more fair for racing.

This is the mod used in several [Balls of Steel](http://www.ballsofsteel.tv/) weekly tournaments, hosted by [Diabetech](http://www.twitch.tv/diabetech).



## Version History

* *1.3* - January 4th, 2016 - Updated the mod for Afterbirth and added some other goodies. Also moved the documentation from the Medium blog to GitHub.
* *1.2* - July 13th, 2105 - Added half a soul heart to Judas. Made modifications to some buggy rooms.
* *1.1* - July 1st, 2015 - The initial public release. The first weekly was played on this version.



## Installation & Uninstallation

Copy all of the files to: `C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\resources\`

To go back to an un-modded game, delete everything in the folder except for the "packed" directory.



## Ruleset

* The mod is meant to be played with Judas.
* The mod is meant to be played on normal mode.
* The mod is meant to be played with the BLCK CNDL seed ("total curse immunity").
* The mod is meant to be played on a "1001%" save file (which is a save file that has everything in the game unlocked). If don't already have one, you can [download one from Speedrun.com](http://www.speedrun.com/saves/fully_unlocked_afterbirth_save_k5imn.zip).
* The mod is meant to be used to race to defeating Blue Baby at the end of the Chest.



## Mod Changes

* All characters start with the D6 (except for Eve, Eden, and Keeper, as it isn't possible).
* The Devil Rooms and Angel Rooms without pedestal items in them have been removed.
* Judas starts with half a soul heart in addition to his 1 red heart container (so that he can consistently take a devil deal).
* Judas starts with a bomb instead of 3 coins (so that he can get into the Treasure Room pedestal surrounded by rocks).
* Cutscene/animation updates from the [Speed Mod](https://raw.githubusercontent.com/Zamiell/speed-mod) have been included.
* More room variety: all rooms in the game will now appear on both easy and hard mode. Additionally, all non-special rooms are now equally likely to occur.
* The charge animations when using Brimstone, Monstro's Lung, Cursed Eye, and Chocolate Milk with some transformations (such as Leviathan) has been fixed.
* Many rooms with unavoidable damage or bugs have been fixed.

### Extra Changes in "Seeded Mode"
* All characters start with The Compass.
* Angel statues are removed and replaced with Key Piece 1.
* Pandora's Box is removed from all item pools.

### Extra Changes for "Dark Room Mode"
* 4 golden chests will now spawn at the beginning of the Dark Room (instead of red chests).
* We Need To Go Deeper! is removed from all item pools.



## Shoutouts

* A huge thanks to [Chronometrics](http://www.twitch.tv/chronometrics) for making and continuing to support Basement Renovator.
* Thanks to all of the racers, I've gathered feedback from, including [Hyphen-ated](http://www.twitch.tv/hyphen_ated), [Cyber_1](http://www.twitch.tv/cyber_1), [Ou_J](http://www.twitch.tv/ou_j), [HauntedQuest](http://www.twitch.tv/hauntedquest), and [Dea1h](http://www.twitch.tv/dea1h).



## Feedback

The changes in this mod are not set in stone. You can discuss the mod with me by contacting me [on Twitch](http://www.twitch.tv/zamiell).



## Documentation of Exact Room Changes

The technical details of the mod are listed here for those who truly care to know all of the specifics.



### Devil Room Buff

* No-item Devil Rooms have been changed to have 1 item. This affects balance in a non-trivial way. Without getting into too much detail, the pros outweigh the cons; a no-item devil deal is disproportionately punishing to a player who has played flawlessly for the entire floor. Furthermore, the overall power increase of a Devil Room becomes more consistent.
* Devil Rooms have been slightly tweaked to have exits on all sides. Otherwise, expected item pedestal amount would change depending on the entrance location.

The changed rooms are as follows:
* #14 (2 black hearts and 1 Imp)
* #5 (red chest chests)

The new room is as follows:
* #16 (1 item, horizontal narrow room)



### Angel Room Buff

Angel Rooms are buffed in a similar manner that Devil Rooms are (for the same reasons). This also has the added benefit of bringing Angel Rooms closer in power to Devil Rooms, making them a viable alternative.

The deleted rooms are as follows:
* #7 (1 eternal heart and 4 soul hearts)
* #4 (2 eternal hearts)
* #3 (3 soul hearts)



### Dople & Evil Twin Fix

When holding down the tear fire button and entering a room with a Dople or Evil Twin, the player is hit with an unavoidable tear. This bug is fixed by changing all the spawn points of the enemies to be near the corner of the room. Once the room is loaded, the enemy will snap back to where they are supposed to be, but the initial buggy tear will not be in line with the player.

The changed rooms are as follows:
* Womb: #56-#62, #114-#118, #259-#261, #289, #301, #598, #605, #625, #646, #661 
* Utero: #56-#62, #114-#117, #259-#261, #289, #301, #598, #605, #624, #646, #661
* Sheol: #19-#24, #42, #56-#57, #61, #166, #181, #188, #196
* Dark Room: #272



### Double Champion Fix

Some rooms have Monstros, Gurdy Jr.'s, or Cages that spawn near an entrance. If the double champion version spawns, they will be touched while the room is loading and automatically take damage. This bug is fixed by moving the enemies closer to the center of the room.

The changed rooms are as follows:
* Sheol: #212 (Cage)
* Chest: #43, #69 (Monstro)
* Chest: #14, #56 (Gurdy Jr.)
* Chest: #34 (Cage)
* The Dark Room: #14, #34 (Cage / Monstro)



### Champion Fistula Fix

Some rooms have Fistulas that spawn near an entrance. If the player is Guppy and has a sufficient number of unused blue flies and the Fistula spawns as the champion Boom Fly version, the flies will kill the Fistula while the room is loading and the player will automatically take damage. This bug is fixed by moving the Fistulas closer to the center of the room.

The changed rooms are as follows:
* Womb: #333
* Utero #333
* Chest: #53, #72, #84



### Boom Fly Fix

Some rooms have Boom Flies next to the entrance. If the player is Guppy and has a sufficient number of unused blue flies, the flies will kill the Boom Fly while the room is loading and the player will automatically take damage. This bug is fixed by moving the Boom Fly closer to the center of the room.

The changed rooms are as follows:
* Caves: #243, #281, #440, #518, #589, #601, #684, #730
* Catacombs: #440, #518, #589, #684, #730



### Begotten Fix

If a player enters from the bottom door of the 2x1 Depths / Necropolis room with the single Begotten, they will automatically take damage. It seems clear that Edmund intended for there to only be a top door in room, so the room has been changed in that manner to fix this bug.

The changed rooms is as follows:
* Depths: #316
* Necropolis - #316



### Clustered Gaping Maws Fix

* If a player with flying and base movement speed gets close to 4 Gaping Maws paired together, it becomes impossible to escape. This was fixed in Womb #424 by adding two Broken Gaping Maws, but the developers forgot to also make the change to Utero #424. I've fixed it for them.
* In both of these rooms, there is no consistent strategy to avoid damage when entering from the bottom-left-hand door. Two pots have been placed to alleviate this.

The changed rooms are as follows:
* Womb: #424
* Utero: #424



### Mulligan Fix

Some rooms have Mulligans that spawn near an entrance. If they explode, the player is hit with unavoidable damage. Alternatively, the Mulligan is too close for the player to reasonably dodge the exploding tear. This bug is fixed by moving the Mulligans closer to the center of the room.

The changed rooms are as follows:
* Basement: #129, #130, #359
* Cellar: #129, #130, #359
* Caves: #548
* Catacombs: #548



### Narrow Krampus Removal

While not technically unavoidable, in a narrow room, Krampus is much more likely to hit the player with an unavoidable spinning Brimstone attack.

The deleted rooms are as follows:
* #2306
* #2305



### Narrow War Removal

While not technically unavoidable, in a narrow room, it is near-impossible to dodge the charge attack of the second phase while at base movement speed.

The deleted room is as follows:
* #4036



### Narrow The Gate Removal

While not technically unavoidable, in a narrow room, there is not enough time to react to the red champion's attack patterns.

The deleted room is as follows:
* #5043


### Narrow Angel Rooms

While not technically unavoidable, they are near-impossible to do safely on a Dr. Fetus build.

The deleted room is as follows:
* Angel Room: #9

The changed rooms are as follows:
* Cathedral: #286, #291



### Narrow Boss Room Door Fix

It is not possible for Devil Room doors to spawn on boss rooms that only have one entrance. For this reason, several rooms were adjusted to allow for at least two entrances.

The changed rooms are as follows:
* #2065 (Fistula)
* #5026 (Dingle)
* #5145 (Gurglings)



### Split Blastocyst Fix

When entering from the top or bottom door of the boss room with the already-split Blastocyst, the player is not given enough time to reasonably dodge the first attack. Two rocks are placed to alleviate this.

The changed room is as follows:
* #2042 (Blastocyst)



### Monstro II & Sucker Fix

When entering from the top or bottom door of the Monstro II boss room with the four Suckers, the player is not given enough time to reasonably dodge the Sucker tear. The Suckers are slightly moved to alleviate this.

The changed room is as follows:
* #1067



### Carrion Queen Fix

In some rooms, Carrion Queen spawns very close to an entrance. This is fixed by moving her slightly closer to the center of the room.

The changed rooms are as follows:
* #3270
* #3272
* #3273



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


### Loki, Lokii, and Death Devil Room Fix

If the player is out of bombs and a Devil Room spawns on the top of the Loki or Loki II room filled with rocks, they will not be able to access it. If the Devil Room spawns on the bottom, the player will be forced to take the boss item in order to see the deal. This is also the case for the Death room filled with pits. This bug is fixed by deleting the rocks/pits respectively.

The changed rooms are as follows:
* #2031 (Loki)
* #3311 (Lokii)
* #4041 (Death)



### Gurdy Maneuverability Fix

In the Gurdy room filled with pits, the player is forced to take the boss item in order to exit the floor. This bug is fixed by deleting some pits to allow for more maneuverability.

The changed rooms are as follows:
* #1066 (Gurdy)




### Magician Card Fix

The rooms with a bugged Magician card are fixed to be a random card.

The changed rooms are as follows:
* Depths: #286
* Necropolis: #286
* Womb: #687
* Utero: #687



### TNT Room Fix

Upon entering certain rooms with TNT barrels, there is a small chance that they will explode. If this occurs with a barrel next to an entrance, the player will take unavoidable damage. This bug is fixed by replacing or removing the barrels in question.

The changed room is as follows:
* Treasure Room: #13
* Pride Mini-Boss Room: #2065
* Basement: #748
* Cellar: #748



### Narrow Red Poop Room Fix

The narrow red poop room in The Chest unavoidable damage on Dr. Fetus builds. This bug has been fixed by deleting some of the poops to allow for a walkable path.

The changed room is as follows:
* The Chest: #289



### Rage Creep & Round Worm Room Fix

One room in the Womb / Utero has two Rage Creeps and four Round Worms in the center. In Afterbirth, the top Rage Creep will hit the player if they stay at the top door. However, this is not unavoidable damage, as it is possible to kill the top Rage Creep before it fires. Alternatively, it is possible to run to the bottom wall before either Rage Creep begins firing. However, the pot in the center of the room messes with the AI of the Round Worms, so the pot has been removed to make traversing this room slightly more consistent.

The changed rooms are as follows:
* Womb: #202
* Utero: #202



### Troll Bomb Room Removal

For certain rooms with troll bombs, there is no consistent strategy to navigate this room without taking damage.

The removed rooms are as follows:
* Basement: #752
* Cellar: #752
* Depths: #699
* Necropolis: #699



### 2x2 Black Bony Fix

In the 2x2 Depths / Necropolis room with Black Bony x8 and pots, the enemies have been spaced out so that they do not automatically become stuck.

The changed rooms are as follows:
* Depths: #731
* Necropolis: #731



### Maggot Room Fix

On the room filled with pits in the Caves, at base damage, Maggots are unavoidable if they decide to path towards you. Furthermore, a Dr. Fetus build has no options with which to dodge the first bomb. This is fixed by moving the Maggots slightly towards the center of the room.

The changed room is as follows:
* Caves: #6



### Sack Fix

If a Sack is near an entrance and it spawns as the white champion version, the player will be touched while the room is loading and automatically take damage. This bug is fixed by moving the Sacks closer to the center of the room.

The changed room is as follows:
* Cellar: #236



### Empty Room Removal

Several rooms in the game are completely empty of any objects at all.

The removed rooms are as follows:
* Basement: #39, #315
* Cellar: #39
* Caves: #170
* Depths: #378, #428
* Sheol: #89
* Cathedral: #57, #89
* Chest: #42



## Rooms That Were Deliberately Not Changed

* Basement #174 - There is a TNT barrel to the left/right of the top/bottom entrances. However, on a knife build, if you are playing correctly, you should be pointing it towards the center of the room upon entering.
* Cellar #766 - This is a room with 3 mega troll bombs, but if you stand completely still, they will not damage you.
* Womb/Utero #147 - This is a room with 3 Nerve Endings next to the entrance. If you have Ipecac, it is possible to use a tear on the wall to safely kill a Nerve Ending. Alternatively, you can safely use a bomb.
* Dark Room #287 - This is a room with 3 mega troll bombs and an Imp. If you stand completely still, the troll bombs will not damage you.
* Mama Gurdy - In Afterbirth, you have more time to dodge the spikes before the hitbox appears.
* Daddy Long Legs - In Afterbirth, the multiple stomp attack no longer damages you before the animation begins.
