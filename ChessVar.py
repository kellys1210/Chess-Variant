User
can you give me a readme for this code 

# Author: Kelly Shields
# GitHub username: kellys1210
# Date: 2/29/2024
# Description: Program which creates a board game which is an abstract variant of chess.

# The following pieces are in play: King, Queen, Knight, Bishop, Rook, Pawn, Hunter, and Falcon.

# The standard pieces begin in their normal starting positions; the Hunter and Falcon pieces
# become eligible to enter when player has 2 major pieces captured (1 can enter after first capture,
# the other can enter after second capture.)

# Pieces move and capture the same as in standard chess, except that there is no check or checkmate, and there is no
# castling, en passant, or pawn promotion.

# If a player's king is captured, the game ends, and that player loses.

class Piece:
    """Initializes chess piece object creation with attributes: color, position, number_moves, captured status, and
    icon. Each individual piece type will inherit from this class. Contains methods for using piece's icon and obtaining
    color and position outside of class.
    """

    def __init__(self, color, position, icon):
        """Initializes Piece objects; attributes: color, position (on board), icon, and captured.
        Each piece will be initialized to their starting position with 0 moves made and not currently captured.
        Icon will be initialized to none and updated in each piece's own class.
        """

        self._color = color
        self._position = position
        self._icon = icon
        self._captured = "NO"

    def get_color(self):
        """Method to allow use of Piece object's color outside of class. Accepts no parameters, returns self._color
        """

        return self._color

    def get_position(self):
        """Method to allow use of Piece object's position outside of class. Accepts no parameters, returns self._position
        """

        return self._position

    def get_icon(self):
        """Method to allow use of Piece object's icon outside of class. Accepts no parameters, returns self._icon
        """

        return self._icon

    def set_captured(self):
        """Method to set piece as captured. Accepts no parameters, no return.
        """

        self._captured = 'YES'


class King(Piece):
    """Class for King piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes King piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        list to list of coordinates corresponding to moves King can make.
        """

        super().__init__(color, position, icon)

        # King can move 1 square in any direction
        self._legal_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def get_legal_moves(self):
        """Method for obtaining King's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        return self._legal_moves


class Queen(Piece):
    """Class for Queen piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Queen piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        to an empty list which will be filled with list of coordinates corresponding to moves Queen can make in
        get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Queen can move any number of squares in any direction
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining Queen's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        # A loop with range of 0-8 to represent rows and columns as indices, iterates through each to generate coordinates
        # for possible positions Queen can move to
        for num in range(8):
            self._legal_moves.append((0, num))      # Move to the right
            self._legal_moves.append((0, -num))     # Move to the left
            self._legal_moves.append((num, 0))      # Move up
            self._legal_moves.append((-num, 0))     # Move down
            self._legal_moves.append((num, num))    # Diagonal right up
            self._legal_moves.append((num, -num))   # Diagonal right down
            self._legal_moves.append((-num, num))   # Diagonal left up
            self._legal_moves.append((-num, -num))  # Diagonal left down

        return self._legal_moves


class Knight(Piece):
    """Class for Knight piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Knight piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        list to list of coordinates corresponding to moves Knight can make.
        """

        super().__init__(color, position, icon)

        # Knight moves in L shape: can move 2 squares and then 1 perpendicular, or 1 square and then 2 perpendicular
        self._legal_moves = [(2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2)]

    def get_legal_moves(self):
        """Method for obtaining Knight's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        return self._legal_moves


class Bishop(Piece):
    """Class for Bishop pieces objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Bishop piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        to an empty list which will be filled with list of coordinates corresponding to moves Bishop can make in
        get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Bishop can move any number of squares diagonally
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining Bishop's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        # A loop with range of 0-8 to represent rows and columns as indices, iterates through each to generate coordinates
        # for possible positions Bishop can move to
        for num in range(8):
            self._legal_moves.append((num, num))  # Diagonal right up
            self._legal_moves.append((num, -num))  # Diagonal right down
            self._legal_moves.append((-num, num))  # Diagonal left up
            self._legal_moves.append((-num, -num))  # Diagonal left down

        return self._legal_moves


class Rook(Piece):
    """Class for Rook piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Rook piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        to an empty list which will be filled with list of coordinates corresponding to moves Rook can make in
        get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Rook can move any numbers of squares along a row or column
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining Rook's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        # A loop with range of 0-8 to represent rows and columns as indices, iterates through each to generate coordinates
        # for possible positions Rook can move to
        for num in range(8):
            self._legal_moves.append((0, num))  # Move to the right
            self._legal_moves.append((0, -num))  # Move to the left
            self._legal_moves.append((num, 0))  # Move up
            self._legal_moves.append((-num, 0))  # Move down

        return self._legal_moves


class Pawn(Piece):
    """Class for Pawn piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, game, color, position, icon):
        """Initializes Pawn piece objects; inherits color, position, and icon from Piece class. Initializes number_moves
        to 0, used to determine whether Pawn piece can move 1 or 2 squares. Initializes 'game' which is a reference to
        ChessVar object, allows get_players_turn method to be utilized in determining which moves are allowed for each
        Pawn piece.
        """

        super().__init__(color, position, icon)

        self._game = game
        self._number_moves = 0

    def get_legal_moves(self):
        """Method for obtaining Pawn's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        # If Pawn piece has not yet moved, can move 2 squares. If it has moved, can only move one square. 'number_moves'
        # count is incremented when move is made. If player is 'WHITE', pieces can only move forward with positive
        # number. If player is 'BLACK', piece can only move forward with negative number (otherwise moving backwards
        # would be legal for pawn, which it is not.)

        if self._game.get_players_turn() == 'WHITE':
            if self._number_moves != 0:
                return [(0, 1), (0, -1)]
            else:
                return [(0, 1), (0, -1), (0, 2), (0, -2)]

        if self._game.get_players_turn() == 'BLACK':
            if self._number_moves != 0:
                return [(0, -1)]
            else:
                return [(0, -1), (0, -2)]

    def set_number_moves(self):
        """Allows Pawn piece number of moves to be incremented to determine if first move has been made/piece
        can no longer move 2 spaces forward
        """

        self._number_moves += 1


class Hunter(Piece):
    """Class for Hunter piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Hunter piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        list to list of coordinates corresponding to moves Hunter can make.
        """

        super().__init__(color, position, icon)

        # Hunter can move forward like a rook, or backward like a bishop.
        self._legal_moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1)]

    def get_legal_moves(self):
        """Method for obtaining Hunter's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        return self._legal_moves


class Falcon(Piece):
    """Class for Falcon piece objects, inheriting from Piece class. Contains method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Falcon piece objects; inherits color, position, and icon from Piece class. Initializes legal_moves
        list to list of coordinates corresponding to moves Falcon can make.
        """

        super().__init__(color, position, icon)

        # Falcon can move forward like a bishop, or backward like a rook.
        self._legal_moves = [(1, 1), (-1, 1), (0, 1), (1, 0), (-1, 0), (0, -1)]

    def get_legal_moves(self):
        """Method for obtaining Falcon's legal move list outside of class. Takes no parameters, returns self._legal_moves
        """

        return self._legal_moves


class Board:
    """Class which contains Board object; board object contains just one attribute of 'board'.
    This represents the 8x8 chess board, which is initialized as a list of 8 lists. Each inner list represents
    a row on the board and each element in the list contains either a piece object (set to standard chess starting
    positions) or set to None if spot starts as empty. Contains a method for displaying the board in its current state
    to the console and a get method for referencing the current state of the board outside the class.
    """

    def __init__(self):
        """Board object initialized with 'board' attribute which is both a functional and visual representation of the
        chess board. Initialized as a list of 8 lists, each element represents a space on the board. The add_piece method
        will add Piece objects to the board.

        The board will be set to beginning positions based on standard chess rules; if a space is occupied, the board
        object contains the Piece object of that piece. If not is not occupied, the board object's position is set to
        None.
        """

        self._board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def print_board(self):
        """Print the current state of the game board. *** This was provided by TA Em for me to use with debugging***"""
        print('The current state of the game board:')
        print('     a    b    c    d    e    f    g    h')
        for row in range(8, 0, -1):
            col_char: int = 97
            cur_row_formatted = []
            for col in range(8):
                square = self._board[row - 1][col]
                if square is not None:
                    cur_row_formatted.append(square.get_icon())
                else:
                    cur_row_formatted.append(' ')
                col_char += 1
            print(f"{row}: {cur_row_formatted}")
        print('\n')

    def add_piece(self, piece, row, column):
        """Method to add Piece objects to board in standard starting positions.
        """

        self._board[row][column] = piece

    def get_board(self):
        """Method to reference current board state outside of method; accepts no parameters, returns board
        """

        return self._board


class ChessVar:
    """Class which creates chess game object. Initializes data members current_state and players_turn to starting positions,
    player move count to 0.
    Initializes capture count to 0, gets/sets game state (unfinished, white won, black won),
    allows player to make a move, allows player to enter fairy pieces, gets/sets current player turn. Contains methods for
    getting/setting game state, getting/setting player turn, making a move, converting string position arguments to
    (x,y) coordinates, and entering fairy piece.
    """

    def __init__(self):
        """Initializes ChessVar attributes: state, players_turn, turn count, and player's captured count and
        if a special piece has been used yet. Also instantiates the Board and Piece classes.
        """

        self._state = 'UNFINISHED'
        self._players_turn = 'WHITE'      # Initialized to white since white player always goes first
        self._turn_count = 0
        self._player1_captures = 0        # To contain captured pieces count
        self._player2_captures = 0
        self._player1_special = None
        self._player2_special = None

        # Instantiates Board
        self._current_board = Board()

        # Instantiates Pieces and adds them to board in Board class in standard starting positions
        # using add_piece method, uses row/column to place pieces on board. Pawn pieces initialized with 'self' attribute
        # to be able to reference ChessVar object within its methods

        self._wK = King('WHITE', 'd1', "♔")
        self._current_board.add_piece(self._wK, 0, 3)

        self._wq = Queen('WHITE', 'e1', "♕")
        self._current_board.add_piece(self._wq, 0, 4)

        self._wk1 = Knight('WHITE', 'b1', "♘")
        self._current_board.add_piece(self._wk1, 0, 1)

        self._wk2 = Knight('WHITE', 'g1', "♘")
        self._current_board.add_piece(self._wk2, 0, 6)

        self._wb1 = Bishop('WHITE', 'c1', "♗")
        self._current_board.add_piece(self._wb1, 0, 2)

        self._wb2 = Bishop('WHITE', 'f1', "♗")
        self._current_board.add_piece(self._wb2, 0, 5)

        self._wr1 = Rook('WHITE', 'a1', "♖")
        self._current_board.add_piece(self._wr1, 0, 0)

        self._wr2 = Rook('WHITE', 'h1', "♖")
        self._current_board.add_piece(self._wr2, 0, 7)

        self._wp1 = Pawn(self, 'WHITE', 'a2', "♙")
        self._current_board.add_piece(self._wp1, 1, 0)

        self._wp2 = Pawn(self, 'WHITE', 'b2', "♙")
        self._current_board.add_piece(self._wp2, 1, 1)

        self._wp3 = Pawn(self, 'WHITE', 'c2', "♙")
        self._current_board.add_piece(self._wp3, 1, 2)

        self._wp4 = Pawn(self, 'WHITE', 'd2', "♙")
        self._current_board.add_piece(self._wp4, 1, 3)

        self._wp5 = Pawn(self, 'WHITE', 'e2', "♙")
        self._current_board.add_piece(self._wp5, 1, 4)

        self._wp6 = Pawn(self, 'WHITE', 'f2', "♙")
        self._current_board.add_piece(self._wp6, 1, 5)

        self._wp7 = Pawn(self, 'WHITE', 'g2', "♙")
        self._current_board.add_piece(self._wp7, 1, 6)

        self._wp8 = Pawn(self, 'WHITE', 'h2', "♙")
        self._current_board.add_piece(self._wp8, 1, 7)

        self._wf = Falcon('WHITE', None, '𓅃')
        self._wh = Hunter('WHITE', None, "↗")

        self._bK = King('BLACK', 'd8', "♚")
        self._current_board.add_piece(self._bK, 7, 3)

        self._bq = Queen('BLACK', 'e8', "♛")
        self._current_board.add_piece(self._bq, 7, 4)

        self._bk1 = Knight('BLACK', 'b8', "♞")
        self._current_board.add_piece(self._bk1, 7, 1)

        self._bk2 = Knight('BLACK', 'g8', "♞")
        self._current_board.add_piece(self._bk2, 7, 6)

        self._bb1 = Bishop('BLACK', 'c8', "♝")
        self._current_board.add_piece(self._bb1, 7, 2)

        self._bb2 = Bishop('BLACK', 'f8', "♝")
        self._current_board.add_piece(self._bb2, 7, 5)

        self._br1 = Rook('BLACK', 'a8', "♜")
        self._current_board.add_piece(self._br1, 7, 0)

        self._br2 = Rook('BLACK', 'h8', "♜")
        self._current_board.add_piece(self._br2, 7, 7)

        self._bp1 = Pawn(self, 'BLACK', 'a7', "♟︎")
        self._current_board.add_piece(self._bp1, 6, 0)

        self._bp2 = Pawn(self, 'BLACK', 'b7', "♟︎")
        self._current_board.add_piece(self._bp2, 6, 1)

        self._bp3 = Pawn(self, 'BLACK', 'c7', "♟︎")
        self._current_board.add_piece(self._bp3, 6, 2)

        self._bp4 = Pawn(self, 'BLACK', 'd7', "♟︎")
        self._current_board.add_piece(self._bp4, 6, 3)

        self._bp5 = Pawn(self, 'BLACK', 'e7', "♟︎")
        self._current_board.add_piece(self._bp5, 6, 4)

        self._bp6 = Pawn(self, 'BLACK', 'f7', "♟︎")
        self._current_board.add_piece(self._bp6, 6, 5)

        self._bp7 = Pawn(self, 'BLACK', 'g7', "♟︎")
        self._current_board.add_piece(self._bp7, 6, 6)

        self._bp8 = Pawn(self, 'BLACK', 'h7', "♟︎")
        self._current_board.add_piece(self._bp8, 6, 7)

        self._bf = Falcon('BLACK', None, "𓅃")
        self._bh = Hunter('BLACK', None, "↗")


    def get_game_state(self):
        """Method for player to determine state of gameplay; takes no parameters, returns:

        "UNFINISHED": game is currently in play
        "WHITE_WON": player playing white pieces has won
        "BLACK_WON": player playing black pieces has won
        """

        return self._state

    def set_game_state(self, current_state):
        """Method for setting state of gameplay; accepts current_state parameter as a string, returns nothing
        """

        self._state = current_state

    def get_players_turn(self):
        """Method to determine whose turn it is; either white or black, used to determine validity of moves, accepts no
        parameters returns player turn.
        """

        return self._players_turn

    def set_players_turn(self, player):
        """Method for setting state of gameplay; accepts current_state parameter as a string, returns nothing
        """

        self._players_turn = player

    def get_turn_count(self):
        """Method to obtain current game's turn count outside of class. Accepts no parameters, returns turn count.
        """

        return self._turn_count

    def make_move(self, moved_from, moved_to):
        """Method that allows player to make a move on the board; parameters accepted are strings representing position
        moved from and position moved to.

        Returns False if:
            - Board space is occupied by own piece
            - Square being moved from does not contain a piece belonging to that player
            - Indicated move is not legal
            - Game has already been won

        Otherwise, returns True, indicated move is made, any captured pieces are removed, game state is updated if
        necessary, and whose turn it is is updated.
        """

        # DEBUG: Print the current state of the game board.
        print(f"Move From: {moved_from}")
        print(f"Move to: {moved_to}")
        self._current_board.print_board()

        # Checks status of game
        if self._state == 'WHITE_WON' or self._state == 'BLACK_WON':
            return False

        # Converts string position to tuple of coordinates
        moved_from_coords = self.convert_to_coords(moved_from)
        moved_to_coords = self.convert_to_coords(moved_to)

        # Checks if moved_from and moved_to position are on board:
        if moved_from_coords[0] not in range(8) or moved_to_coords[1] not in range(8):
            return False
        if moved_to_coords[0] not in range(8) or moved_to_coords[1] not in range(8):
            return False

        # Allows Board object's current board to be referenced
        board = self._current_board.get_board()

        # Checks if moved_to space is occupied by own piece
        if board[moved_to_coords[1]][moved_to_coords[0]] is not None:
            moved_to_color = board[moved_to_coords[1]][moved_to_coords[0]].get_color()
            if self._players_turn == moved_to_color:
                return False

        # Checks if square being moved from contains piece belonging to current player
        if board[moved_from_coords[1]][moved_from_coords[0]] is not None:
            piece_color = board[moved_from_coords[1]][moved_from_coords[0]].get_color()
            if piece_color != self._players_turn:
                return False
        else:
            return False

        # Checks if move is legal
        piece = board[moved_from_coords[1]][moved_from_coords[0]]  # Obtains piece object at current position
        piece_legal_moves = piece.get_legal_moves()

        row_from, column_from = moved_from_coords
        row_to, column_to = moved_to_coords

        # Calculates if move is legal by obtaining difference between moved_to coordinates from moved from coordinates;
        # checks if difference coordinates is in legal moves list. If not, move is not valid and returns False
        row_diff = row_to - row_from
        column_diff = column_to - column_from

        diff_coords = row_diff, column_diff

        if diff_coords in piece_legal_moves:

            # Checks for pieces in path, return False if path is not clear
            if row_from == row_to:  # Moving vertically
                if column_from < column_to:
                    move = 1  # Moving forward
                else:
                    move = -1  # Backward
                position = column_from + move
                while position != column_to:
                    if board[row_from][position] is not None:
                        return False
                    position += move

            elif column_from == column_to:  # Moving horizontally
                if row_from < row_to:
                    move = 1   # to right
                else:
                    move = -1  # to left
                position = row_from + move
                while position != row_to:
                    if board[position][column_from] is not None:
                        return False
                    position += move

            # Checks for capture, if so removes piece and puts piece in player's captured list. Checks to verify if
            # piece in moved_to spot belongs to other player; if so, eligible for capture. If piece being captured is not
            # a pawn, then player's capture count is incremented in order to be able to use in fairy piece eligibility.
            moved_to_piece = board[moved_to_coords[1]][moved_to_coords[0]]
            if moved_to_piece is not None:
                if isinstance(piece, Pawn):  # Since Pawn can only capture diagonally, not ahead
                    return False
                else:
                    if self._players_turn != moved_to_piece.get_color():
                        moved_to_piece.set_captured()
                        if not isinstance(moved_to_piece, Pawn):
                            if self._players_turn == 'WHITE':
                                self._player1_captures += 1
                            else:
                                self._player2_captures += 1

                    # Updates game status if necessary, sets to current payer won if King was captured :
                    if isinstance(moved_to_piece, King):
                        self._state = (f'{self._players_turn}_WON')

            # Moves piece to new board position, sets old position to empty
            board[moved_to_coords[1]][moved_to_coords[0]] = piece
            board[moved_from_coords[1]][moved_from_coords[0]] = None

            # If pawn piece moved, increments turn count
            if isinstance(piece, Pawn):
                piece.set_number_moves()

            # Update player turn only if move was successful
            if self._players_turn == 'WHITE':
                self._players_turn = 'BLACK'
            else:
                self._players_turn = 'WHITE'
                self._turn_count += 1

            return True  # move completed

        # if piece is Pawn and move not in legal moves, checks if capture is possible; if move is diagonal in front
        # and there is no piece there, return False. If there is an opposing player's piece, it can be captured and
        # returns True
        if isinstance(piece, Pawn) and piece.get_color() == 'WHITE':
            if diff_coords in [(-1, 1), (1, 1)]:
                if board[moved_to_coords[1]][moved_to_coords[0]] is not None:
                    if board[moved_to_coords[1]][moved_to_coords[0]].get_color() == 'BLACK':
                        board[moved_to_coords[1]][moved_to_coords[0]] = piece
                        board[moved_from_coords[1]][moved_from_coords[0]] = None
                        self._players_turn = 'BLACK'
                        return True
                return False

        if isinstance(piece, Pawn) and piece.get_color() == 'BLACK':
            if diff_coords in [(-1, -1), (1, -1)]:
                if board[moved_to_coords[1]][moved_to_coords[0]] is not None:
                    if board[moved_to_coords[1]][moved_to_coords[0]].get_color() == 'WHITE':
                        board[moved_to_coords[1]][moved_to_coords[0]] = piece
                        board[moved_from_coords[1]][moved_from_coords[0]] = None
                        self._players_turn = 'WHITE'
                        return True
                return False
        return False

    def convert_to_coords(self, moving_position):
        """Method to convert position from string argument to coordinate representation. Utilizes dictionary of
        corresponding alphabetical:numerical values to change alphabetical character to numerical representation.
        Parameters are string value of moving position, called by 'make_move' method. Returns a tuple of coordinate values.
        """

        alpha_num_dict = {
            'a' : 0,
            'b' : 1,
            'c' : 2,
            'd' : 3,
            'e' : 4,
            'f' : 5,
            'g' : 6,
            'h' : 7,
        }

        x = alpha_num_dict[moving_position[0]]
        y = int(moving_position[1])
        y -= 1  # Because list indices start at 0

        return (x, y)

    def enter_fairy_piece(self, type, entry_position):
        """Method that allows player to enter fairy piece into gameplay; parameters accepted are strings representing
        type of piece being entered (white falcon: 'F', black falcon: 'f', white hunter: 'H', black hunter: 'h'), and
        board position piece is to be placed.

        Returns False if fairy piece is not allowed to enter board at that time/position.

        Otherwise, returns True.

        Must check: Game status, if it is that players turn, if position on board is open, if position is player's
        home rank, if player is qualified to enter fairy piece.
        """

        # Checks status of game, returns False if game is over
        if self._state == 'WHITE_WON' or self._state == 'BLACK_WON':
            return False

        # Converts type entered to Piece object
        if type == 'F':
            fairy_piece = self._wf
        if type == 'f':
            fairy_piece = self._bf
        if type == 'H':
            fairy_piece = self._wh
        if type == 'h':
            fairy_piece = self._bh

        # Changes entry position to coordinates
        entry_position = self.convert_to_coords(entry_position)

        # Checks if it's that player's turn
        if fairy_piece.get_color() != self._players_turn:
            return False

        # Checks if moved_to space is occupied; if so, returns False
        board = self._current_board.get_board()
        if board[entry_position[1]][entry_position[0]] is not None:
            return False

        # Checks if entry position is in player's home rank; if not, returns False
        if self._players_turn == 'WHITE':
            if entry_position[1] < 3:     # If y coordinate is over 2, not in white player's home rank
                return False

        if self._players_turn == 'BLACK':
            if entry_position[1] > 7:
                return False           # If y coordinate is less than 7, not in white player's home rank

        # Checks if player has had major pieces captured. Must have at least 1 captured to enter first fairy piece and
        # at least 2 captured to enter second
        if self._players_turn == 'WHITE':
            if self._player1_special == 0:
                if self._player1_captures < 1:
                    return False
            else:
                if self._player1_captures < 2:
                    return False

        if self._players_turn == 'BLACK':
            if self._player2_special == 0:
                if self._player2_captures < 1:
                    return False
            else:
                if self._player2_captures < 2:
                    return False

        # If valid, piece is place on board at entry point
        board[entry_position[1]][entry_position[0]] = fairy_piece

        # Update player turn, changes turn count if necessary (increments count when changing to white)
        if self._players_turn == 'WHITE':
            self._players_turn = 'BLACK'
        else:
            self._players_turn = 'WHITE'
            self._turn_count += 1

        return True


game = ChessVar()
