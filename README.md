# Abstract Variant of Chess

This is an abstract variant of chess implemented in Python, featuring standard chess pieces along with additional fairy pieces, the Hunter and Falcon. This variant introduces unique rules while maintaining the core mechanics of movement and capture from traditional chess.

## Table of Contents

- [Game Overview](#game-overview)
- [Setup](#setup)
- [Game Rules](#game-rules)
- [Special Pieces](#special-pieces)
- [Board Display](#board-display)
- [Commands](#commands)
- [License](#license)

## Game Overview

ChessVar follows the basic principles of chess gameplay but includes some variations and special pieces:

- **Pieces in Play**: King, Queen, Knight, Bishop, Rook, Pawn, Hunter, Falcon.
- **Special Pieces**: Hunter and Falcon enter the game after a player has captured two major pieces.

## Setup

Ensure you have Python installed to run the game locally. Clone the repository:

```bash
git clone https://github.com/kellys1210/ChessVar.git
cd ChessVar
```

### Run the game:

```bash
python main.py
```

Follow the prompts to make moves and enter fairy pieces when eligible.

## Game Rules

*   **Movement and Capture**: Pieces move and capture as in standard chess.
    
*   **Winning Condition**: Capture the opponent's King to win.
    
*   **Special Rules**: No check or checkmate, no castling, en passant, or pawn promotion.
    

## Special Pieces

### Hunter

*   Moves forward like a Rook or backward like a Bishop.
    

### Falcon

*   Moves forward like a Bishop or backward like a Rook.
    

## Board Display

The board is displayed in ASCII with pieces represented by Unicode symbols:

  a b c d e f g h
8 r n b q k b n r 
7 p p p p p p p p 
6 . . . . . . . . 
5 . . . . . . . . 
4 . . . . . . . . 
3 . . . . . . . . 
2 P P P P P P P P 
1 R N B Q K B N R 


## Commands

*   **make\_move(from\_position, to\_position)**: Make a move on the board.
    
*   **enter\_fairy\_piece(type, entry\_position)**: Enter a fairy piece onto the board.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

