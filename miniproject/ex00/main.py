from checkmate import checkmate

def main():
    print("=== Case 1: King is in check ===")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)

    print("\n=== Case 2: King is safe ===")
    board2 = """\
R...
....
..K.
....\
"""
    checkmate(board2)

    print("\n=== Case 3: Invalid board (Error) ===")
    board3 = """\
R....
.K..
..P.\
"""
    checkmate(board3)

if __name__ == "__main__":
    main()
