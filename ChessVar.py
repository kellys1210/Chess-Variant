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
    """Initializes a chess piece object with attributes such as color, position, number of moves, captured status, and icon.
    Each individual piece type will inherit from this class. Contains methods for using the piece's icon and obtaining
    color and position outside of the class.
    """

    def __init__(self, color, position, icon):
        """Initializes Piece objects with attributes: color, position (on board), icon, and captured.
        Each piece is initialized to its starting position with 0 moves made and not currently captured.
        The icon is initialized to None and updated in each piece's own class.
        """

        self._color = color
        self._position = position
        self._icon = icon
        self._captured = "NO"

    def get_color(self):
        """Method to allow access to the color of the Piece object outside of the class.
        Accepts no parameters, returns self._color.
        """
        return self._color

    def get_position(self):
        """Method to allow access to the position of the Piece object outside of the class.
        Accepts no parameters, returns self._position.
        """
        return self._position

    def get_icon(self):
        """Method to allow access to the icon of the Piece object outside of the class.
        Accepts no parameters, returns self._icon.
        """
        return self._icon

    def set_captured(self):
        """Method to set the piece as captured.
        Accepts no parameters, no return.
        """
        self._captured = 'YES'


class King(Piece):
    """Class for King piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes King piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves list to a list of coordinates corresponding to moves the King can make.
        """

        super().__init__(color, position, icon)

        # King can move 1 square in any direction
        self._legal_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def get_legal_moves(self):
        """Method for obtaining the King's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
        return self._legal_moves


class Queen(Piece):
    """Class for Queen piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Queen piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves to an empty list which will be filled with a list of coordinates corresponding to moves the Queen can make in the get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Queen can move any number of squares in any direction
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining the Queen's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
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
    """Class for Knight piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Knight piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves list to a list of coordinates corresponding to moves the Knight can make.
        """

        super().__init__(color, position, icon)

        # Knight moves in L shape: can move 2 squares and then 1 perpendicular, or 1 square and then 2 perpendicular
        self._legal_moves = [(2, 1), (-2, 1), (1, 2), (-1, 2), (2, -1), (-2, -1), (1, -2), (-1, -2)]

    def get_legal_moves(self):
        """Method for obtaining the Knight's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
        return self._legal_moves


class Bishop(Piece):
    """Class for Bishop piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Bishop piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves to an empty list which will be filled with a list of coordinates corresponding to moves the Bishop can make in the get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Bishop can move any number of squares diagonally
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining the Bishop's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
        for num in range(8):
            self._legal_moves.append((num, num))    # Diagonal right up
            self._legal_moves.append((num, -num))   # Diagonal right down
            self._legal_moves.append((-num, num))   # Diagonal left up
            self._legal_moves.append((-num, -num))  # Diagonal left down
        return self._legal_moves


class Rook(Piece):
    """Class for Rook piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Rook piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves to an empty list which will be filled with a list of coordinates corresponding to moves the Rook can make in the get_legal_moves method.
        """

        super().__init__(color, position, icon)

        # Rook can move any number of squares horizontally or vertically
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining the Rook's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
        for num in range(8):
            self._legal_moves.append((0, num))      # Move to the right
            self._legal_moves.append((0, -num))     # Move to the left
            self._legal_moves.append((num, 0))      # Move up
            self._legal_moves.append((-num, 0))     # Move down
        return self._legal_moves


class Pawn(Piece):
    """Class for Pawn piece objects, inheriting from the Piece class. Contains a method for creating/obtaining legal moves.
    """

    def __init__(self, color, position, icon):
        """Initializes Pawn piece objects; inherits color, position, and icon from the Piece class.
        Initializes legal_moves list to a list of coordinates corresponding to moves the Pawn can make.
        """

        super().__init__(color, position, icon)

        # Pawn can move forward 1 square, 2 squares on first move, and capture diagonally
        self._legal_moves = []

    def get_legal_moves(self):
        """Method for obtaining the Pawn's legal move list outside of the class.
        Takes no parameters, returns self._legal_moves.
        """
        # White pawn moves
        if self._color == 'white':
            self._legal_moves.append((0, 1))        # Move forward 1
            if self._position[1] == 1:              # If pawn is at starting position
                self._legal_moves.append((0, 2))    # Move forward 2
            self._legal_moves.append((-1, 1))      # Capture diagonally left
            self._legal_moves.append((1, 1))       # Capture diagonally right
        # Black pawn moves
        else:
            self._legal_moves.append((0, -1))       # Move forward 1
            if self._position[1] == 6:              # If pawn is at starting position
                self._legal_moves.append((0, -2))   # Move forward 2
            self._legal_moves.append((-1, -1))     # Capture diagonally left
            self._legal_moves.append((1, -1))      # Capture diagonally right
        return self._legal_moves



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
    """Class for the chess board. Initializes an 8x8 grid with Piece objects representing the current state of the game.
    Contains methods for initializing the board, displaying the board, moving pieces, and checking for checkmate.
    """

    def __init__(self):
        """Initialize the board with None values to represent empty squares."""
        self._board = [[None] * 8 for _ in range(8)]

    def print_board(self):
        """Print the current state of the board."""
        print('  a b c d e f g h')
        for row, row_data in enumerate(self._board[::-1], 1):
            print(row, end=' ')
            for piece in row_data:
                if piece is not None:
                    print(piece.get_icon(), end=' ')
                else:
                    print('.', end=' ')
            print()

    def add_piece(self, piece, row, column):
        """Add a piece to the board at the specified position."""
        self._board[row][column] = piece

    def get_board(self):
        """Return the current state of the board."""
        return self._board

class ChessVar:
    """Class representing a chess game with attributes representing: game state, current player's turn, how many turns have
    occurred, how many pieces each player has captured, and how many special pieces each player has entered. Initializes objects 
    for Board class and initializes chess pieces.
    """

    def __init__(self):
        """Initialize ChessVar attributes."""
        self._state = 'UNFINISHED'
        self._players_turn = 'WHITE'
        self._turn_count = 0
        self._player1_captures = 0
        self._player2_captures = 0
        self._player1_special = 0
        self._player2_special = 0
        self._current_board = Board()
        self._initialize_pieces()

    def _initialize_pieces(self):
        """Initialize pieces on the board."""
        # White pieces
        white_pieces = [('♔', King), ('♕', Queen), ('♘', Knight), ('♗', Bishop),
                        ('♖', Rook), ('♙', Pawn)]
        for row, piece_type in enumerate(white_pieces, start=1):
            for col in range(8):
                piece_symbol, piece_class = piece_type
                piece = piece_class('WHITE', None, piece_symbol)
                self._current_board.add_piece(piece, row - 1, col)
        # Black pieces
        black_pieces = [('♚', King), ('♛', Queen), ('♞', Knight), ('♝', Bishop),
                        ('♜', Rook), ('♟', Pawn)]
        for row, piece_type in enumerate(black_pieces, start=7):
            for col in range(8):
                piece_symbol, piece_class = piece_type
                piece = piece_class('BLACK', None, piece_symbol)
                self._current_board.add_piece(piece, row - 1, col)

    def _initialize_fairy_pieces(self):
        """Initialize fairy pieces without placing on board."""
        self._wf = Falcon('WHITE', None, '𓅃')
        self._wh = Hunter('WHITE', None, "↗")
        self._bf = Falcon('BLACK', None, '𓅃')
        self._bh = Hunter('BLACK', None, "↗")

    def get_game_state(self):
        """Get the current state of the game."""
        return self._state

    def set_game_state(self, state):
        """Set the state of the game."""
        self._state = state

    def get_players_turn(self):
        """Get the current player's turn."""
        return self._players_turn

    def set_players_turn(self, player):
        """Set the current player's turn."""
        self._players_turn = player

    def get_turn_count(self):
        """Get the number of turns."""
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

        # Check if the moved-to space is occupied by the player's own piece
        if board[moved_to_coords[1]][moved_to_coords[0]] is not None:
            moved_to_color = board[moved_to_coords[1]][moved_to_coords[0]].get_color()
            if self._players_turn == moved_to_color:
                return False

        # Check if the square being moved from contains a piece belonging to the current player
        if board[moved_from_coords[1]][moved_from_coords[0]] is None:
            return False

        piece_color = board[moved_from_coords[1]][moved_from_coords[0]].get_color()
        if piece_color != self._players_turn:
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

            #Checks for capture and, if found, removes the captured piece, placing it in the player's capture list. 
            #Verifies if the piece in the destination spot belongs to the opponent, making it eligible for capture. 
            #If the captured piece is not a pawn, increments the player's capture count for fairy piece eligibility.
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
