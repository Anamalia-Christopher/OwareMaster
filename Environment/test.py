from main import Oware
from random import randrange

def playnext(obj, position):
    if obj.next:
        return obj.player2(position)

    obj.player1(position)

game = Oware()
if game.who_starts==0:
    game.player1(randrange(1,7))
else:
    game.player2(randrange(1,7))

while True:
    playnext(game,randrange(1,7) )
    if sum(game.score)==48:
        break




