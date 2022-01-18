# War-Game

The game is implemented in Python. The objective of the game is to win all of the cards. For more details about the game refer this [link](https://en.wikipedia.org/wiki/War_(card_game)).

#### Assumptions

- The deck is divided evenly among the players (in this case two).
- Aces are high, and suits are ignored.


#### Corner cases

- If a player runs out of cards during a war that player immediately loses.
- If both the players runs out of cards during a war, then no one wins.


#### Things done differently if given more time

- Make this a multiplayer game with more than two players.
- Wrap this in a flask server and hosted it on an ec2 instance to allow players to play online.
- Allow for user input for every turn with automatic play as the fallback, that is if player doesn’t play in time then computer plays automatically.
 


