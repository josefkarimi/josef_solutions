import random
print("salam")
class X0:

    def __init__(self, boardsize = 3, players = 2):
        self.board = []
        self.boardsize = boardsize
        self.players = players
        self.list_of_players = self.players_list()
   
    def players_list(self):
        self.list_of_players = []
        if self.players <= 26:
            for i in range(self.players):
                self.list_of_players.append(chr(i+97))

        elif self.player <= 52:
            for i in range(26):
                self.list_of_players.append(chr(i+97))
            for i in range(self.players-26):
                self.list_of_players.append(chr(i+65))
        else:
            raise ValueError("too many players") 
        return self.list_of_players

            

    def create_board(self):
        for i in range(self.boardsize):
            row = []
            for j in range(self.boardsize):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(1, self.players)

    def fix_spot(self, row, col, player):
        if self.board[row][col] == "-":
            self.board[row][col] = player
        else:
            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)            


    def is_player_win(self, player):
        win = None

        n = self.boardsize

        # checking rows
        for i in range(n):
            win = False
            for j in range(n-2):
                if self.board[i][j] != "-" and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] :
                    win = True
                    break
            if win:
                return win

        # checking columns
        for i in range(n-2):
            win = False
            for j in range(n):
                if self.board[i][j] != "-" and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j]:
                    win = True
                    break
            if win:
                return win

        # checking diagonals
        win = False
        for x in range(n-2):
            for y in range(n-2):
                if self.board[x][y] != "-" and self.board[x][y] == self.board[x+1][y+1] == self.board[x+2][y+2]:
                    win = True
                    break
                if self.board[x][y+2] != "-" and self.board[x][y+2] == self.board[x+1][y+1] == self.board[x+2][y]:
                    win = True
        return win


    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        print(self.list_of_players)
        try:
            return self.list_of_players.pop(0)
        except:
            self.players_list()
            return self.list_of_players.pop(0)

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = self.list_of_players.pop(0)
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = X0(boardsize = int(input("please enter the board size:")), players= int(input("please enter the number of players:")))
tic_tac_toe.start()
