def checkmate(board):
    try:
        lines = [line for line in board.strip().split('\n') if line]
        n = len(lines)
        if n == 0 or any(len(line) != n for line in lines):
            print("Error")
            return

        kings = [(i, j) for i in range(n) for j, ch in enumerate(lines[i]) if ch == 'K']
        if len(kings) != 1:
            print("Error")
            return
        xk, yk = kings[0]

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < n

        for x in range(n):
            for y in range(n):
                p = lines[x][y]
                if p == '.' or p == 'K':
                    continue

                dx = xk - x
                dy = yk - y

                if p == 'P' and dx == -1 and abs(dy) == 1:
                    print("Success")
                    return

                if p == 'R' and (dx == 0 or dy == 0):
                    step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
                    step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
                    cx, cy = x + step_x, y + step_y
                    while in_bounds(cx, cy):
                        if (cx, cy) == (xk, yk):
                            print("Success")
                            return
                        if lines[cx][cy] != '.':
                            break
                        cx += step_x
                        cy += step_y

                if p == 'B' and abs(dx) == abs(dy) and dx != 0:
                    step_x = 1 if dx > 0 else -1
                    step_y = 1 if dy > 0 else -1
                    cx, cy = x + step_x, y + step_y
                    while in_bounds(cx, cy):
                        if (cx, cy) == (xk, yk):
                            print("Success")
                            return
                        if lines[cx][cy] != '.':
                            break
                        cx += step_x
                        cy += step_y

                if p == 'Q' and (abs(dx) == abs(dy) or dx == 0 or dy == 0):
                    step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
                    step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
                    cx, cy = x + step_x, y + step_y
                    while in_bounds(cx, cy):
                        if (cx, cy) == (xk, yk):
                            print("Success")
                            return
                        if lines[cx][cy] != '.':
                            break
                        cx += step_x
                        cy += step_y

        print("Fail to checkmate")
    except:
        print("Error")
        