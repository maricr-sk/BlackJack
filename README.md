# CardGame
A project that is creating the Black Jack cardgame. 

Directions: 

Black Jack is a popular casino game played with a standard 52-card deck. A single player plays against the "dealer".

Basic rules: In the first part of the game, the player is dealt cards repeatedly until one of the following events happens: 

The player's score (i.e., the sum of the values of the player's cards, explained below) reaches 21. In this case, the player wins immediately.
The player's score exceed 21. In this case, the player loses immediately. 
The player decides to "stay", i.e., not take any more cards. 
If the player has neither won or lost at this point, it is the dealer's turn to draw cards. The dealer keeps drawing cards until the sum of their card values is 17 or higher. Then the dealer stops and the winner is determined as follows: 

If the dealer's score reaches 21, the dealer wins.
If the dealer's score exceeds 21, the player wins.
If the sum of the card values of the player and the dealer are equal, the game is a "push" and nobody wins. 
Otherwise, the person with the highest score wins.
Note that the dealer's behavior is completely deterministic -- the dealer must take another card if their value is less than 17 and must stay if the value exceeds 17 (unless the dealer has already lost by that point).

The value of an Ace card is normally 11, unless this would result in a total score of more than 21. In that case, the value of the Ace is 1. Note that this means that the value of the Ace card may change during the game. Assume the player initially draws an Ace (value 11), then a 2 (so the total value becomes 13), and then a Queen. This would bring the total value to 23, but at this point the value of the Ace changes to 1, so the total value of the hand is actually only 1+2+10=13.

Here is example output for a game of Black Jack. Your program does not have to mimic this output precisely. 

You drew ♥9.

sum: 9

Do you want another card? (y/n)y

You drew ♠Q.

sum: 19

Do you want another card? (y/n)n

My turn.

I drew ♦4

My sum: 4

I drew ♦6

My sum: 10

I drew ♦3

My sum: 13

I drew ♠3

My sum: 16

I drew ♦8

My sum: 24

You win.
