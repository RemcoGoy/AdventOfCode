def main():
    f = open("input.txt")
    content = f.readlines()
    
    drawn_numbers = content[0].split(",")
    boards = setup_boards(content)
    
    board_won = None
    last_n = None
    already_won = []
    last_won = None
    for number in drawn_numbers:
        for board in boards:
            for line in board:
                for n in line:
                    if n["key"] == number:
                        n["found"] = True
        
        board_won = check_boards(boards, already_won)
        if len(board_won) > 0:
            last_n = number 
            already_won.extend(board_won)
            print(board_won, last_n)
            if (len(board_won) == 1):
                last_won = board_won[0]
                last_board = boards[last_won][:]
                if len(already_won) == len(boards):
                    break
    
    unmarked = unmarked_numbers(last_board)
    print(unmarked * int(last_n))
    f.close()

def unmarked_numbers(board):
    unmarked = 0
    for line in board:
        for n in line:
            if not n["found"]:
                unmarked += int(n["key"])
    
    return unmarked

def check_boards(boards, already_won):
    won = []
    for i, board in enumerate(boards):
        done = False
        for line in board:
            done = all(x["found"] for x in line)
            if done:
                break
        
        for index in range(len(board[0])):
            col_done = True
            for j in range(len(board)):
                col_done = board[j][index]["found"]
                if not col_done:
                    break
            
            if col_done:
                break
        
        if done or col_done:
            if i not in already_won:
                won.append(i)
    
    return won

def setup_boards(content):
    boards = []
    for i in range(2, len(content), 6):
        board = []
        for j in range(5):
            board_row = map(lambda x: {"key": x, "found": False}, content[i + j].strip("\n").split())
            board.append(board_row)
        boards.append(board)
    
    return boards

if __name__ == "__main__":
    main()