# Room Changes - Balance

Some rooms were purely changed for balance (racing) reasons. Rooms with bug fixes are below in a different section.

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

### Treasure Room Fix for Judas

The Treasure Room with two pedestals and spikes has been slightly tweaked so that Judas can use a bomb to get the item without spending a soul heart.

The changed room is as follows:
* Treasure Room: #21

<br />

### Trapdoor Room

On Sheol, there exists a room with a trapdoor that takes you directly to the Dark Room without having to fight Satan. This puts too much of an extreme lower bound on the clear time of the floor.

The removed room is as follows:
* Sheol: #290

<br />

# Room Changes - Bug Fixes

The Jud6s mod tries to fix as many bugs as possible. The technical details of all of the room changes in the mod are listed here for those who want to know the specifics.

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
* Chest: #14, #56 (Gurdy Jr.)
* Chest: #34 (Cage)
* Chest: #43, #69 (Monstro)
* Chest: #301 (Gurglings)
* The Dark Room: #14, #83 (Cage)
* The Dark Room: #34 (Monstro)

<br />

### Forsaken Fix

If a Forsaken does a Brimstone attack in the middle of a L-shaped room, it can sometimes be unavoidable.

The deleted rooms are as follows:
* Chest: #295, #296

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
* Depths: #16 (Brain)
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
* Womb: #507
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
* Depths: #226, #417
* Necropolis: #226, #417
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

### Donation Machine Room Removal

One room in the Necropolis has a donation machine in it. Since using the BLCK CNDL seed removes donation machines from the game, this room is largely useless.

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
* Cathedral: #57, #73, #89
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
* Basement: #581
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
* Pride (narrow room) - Sometimes, the bombs spawn in such a way that it is unavoidable damage, but this is rare.
