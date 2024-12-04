## Part 1: Filter all possible games where no set exceeds the maximum allowed number of cubes for any color.

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue  
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red  
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red  
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green  
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

### Approach:

1. Process each game and get information of each set.
2. For each set, store its details in the dictionary named `game_set_dict` with the following keys:

   - "game number": The game identifier.
   - "set number": The position of the set within the game.
   - "red", "green", "blue": The count of cubes for each color.

3. Create Dataframe of all game trials by combining all the `game_set_dict` entries.
4. Filter valid rows where no set exceeds the maximum allowed number of cubes for any color.
5. Calculate sum of all such game ids.

## Part 2: Power of sets containing the minimum number of cubes that must be present for a game.

### Approach:

1. Group rows of the dataframe by game ids and calulate maximum count of cubes of each color.
2. Multiply the maximum counts of the three colors to calculate the "power" of the minimal set required for the game.
3. Sum up the computed powers for all games to obtain the final result.
