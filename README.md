# Water_Tank_Game

Water Tank is a competitive card game played between two players (a human player and a computer). Each player starts with an empty water tank,
which they need to fill. The goal is to be the first player to fill their tank. A tank is filled if it
reaches the value of 75 to 80 units (inclusive). The human player’s moves are decided by the
user playing the game, by asking for input, and the computer’s moves are decided by the
program.

There are two types of cards: water cards and power cards. There will be a pile for each type
of card (one pile for water and one pile for power). Each water card has a value that represents
the amount of water that it contributes to the tank. When a water card is played, that player
adds the specified amount of water to their tank. Power cards allow players to perform special
actions:
* SOH (Steal Opponent’s Half): Take half the water in your opponent’s tank and add it to
your own
* DOT (Drain Opponent’s Tank): Empty your opponent’s tank completely
* DMT (Double My Tank): Double the current value of your own tank

Players take turns either using a card or discarding a card. If a player discards a card, it goes to
the bottom (last index) of its respective pile. Once the player has used or discarded a card, they
draw a new card, from the top of the pile (index 0), of the same type as the card they just used
or discarded.

If a player’s water level exceeds their tank’s maximum fill value, an overflow happens. In the
case of an overflow, extra water sloshes out of the tank. The amount of water that remains in
the tank is determined by a formula: remaining water = maximum fill value - overflow
1Introduction to Software Development

For example, if a player’s tank level goes to 90, and its maximum fill value is 80, the overflow
is 10. Deduct 10 from the maximum fill value to find the remaining water in the tank, which is
70 in this case.

The game continues in turns until one player’s tank is filled. A tank is considered filled when
the tank level is between the minimum and maximum fill values (inclusive). The first player to
fill their tank wins the game.
