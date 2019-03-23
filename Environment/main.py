from random import choice
# start the game
# end the game
# playing the game
# keep the score

class Oware:
    def __init__(self):

        self.START_GAME()
        self.game1D()
        self.score = [0,0]


    def START_GAME(self):
        self.board = [[ 4 for i in range(6)]for j in range(2)]
        self.who_starts = choice([0,1])
        return

    def END_GAME(self):
        self.game2D()
        self.score[0] +=sum(self.board[0])
        self.score[1] +=sum(self.board[1])
        self.scores()
        return print('done')


    def play(self):
        position = self.position

        while True:

            marbles= self.board[position]

            self.board[position] = 0
            for i in range(marbles):
                position +=1
                if position==12:
                    position=0

                self.board[position] +=1
                if 6*self.player<position<(6*(self.player+1)-1) and self.board[position]==4:
                    self.score[self.player] +=4
                    self.board[position] = 0

            print(self.board, self.player)
            if self.board[position]==1 or self.board[position]==0:
                break

        self.__next__()

        if sum(self.score)>=40:
            self.END_GAME()
        return



    def __next__(self):
        if self.player ==1:
            self.next =0
        else:
            self.next =1

    def player1(self, position):
        self.inputChecker(position)

        self.player = 0

        # position given by the player is between 1-6
        self.position = position-1

        if self.accepted_move():
            return self.play()

        return


    def player2(self, position):
        self.inputChecker(position)

        self.player = 1

        # position given by the player is between 1-6
        self.position = 6+position-1
        if self.accepted_move():
            return self.play()

        return

    def accepted_move(self):
        if self.board[self.position]:
            return True
        return False


    def score_player1(self):
        return self.score[0]

    def score_player2(self):
        return self.score[1]

    def scores(self):
        return print('player1: %d -- player2: %d ' %(self.score[0], self.score[1]) )

    def inputChecker(self, position):
        if 1<=position<=6:
            return

        else:
            print('number from 1-6')
            exit()



    def game2D(self):
        if len(self.board)==12:
            self.board = [self.board[0:6], self.board[6::]]
            return
        return print('in 2D already')


    def game1D(self):
        if len(self.board)==2:
            self.board = [j for i in self.board for j in i]
            return
        return print('in 1D already')

    def __str__(self):
        self.game2D()
        return str(self.board)


# gudlucsam
# mustaphatidooyussif