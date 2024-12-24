class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.symbol = ""

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(9)]

    def change_cell_state(self, cell_number, symbol):
        if 0 <= cell_number < 9 and not self.cells[cell_number].is_occupied:
            self.cells[cell_number].is_occupied = True
            self.cells[cell_number].symbol = symbol
            return True
        return False

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # строки
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Столбцы
            [0, 4, 8], [2, 4, 6]             # диоганали
        ]
        for combo in win_combinations:
            symbols = [self.cells[i].symbol for i in combo]
            if symbols[0] == symbols[1] == symbols[2] != "":
                return True
        return False

    def is_draw(self):
        return all(cell.is_occupied for cell in self.cells)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.wins = 0
        self.symbol = symbol

    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки (1-9): ")) - 1
                if 0 <= move < 9:
                    return move
                else:
                    print("Некорректный номер клетки.")
            except ValueError:
                print("Некорректный ввод.")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def play_round(self):
        move = self.current_player.make_move()
        if self.board.change_cell_state(move, self.current_player.symbol):
            if self.board.check_win():
                print(f"Победил {self.current_player.name}!")
                self.current_player.wins += 1
                return True
            elif self.board.is_draw():
                print("Ничья!")
                return True
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        else:
            print("Клетка занята. Попробуйте ещё раз.")
        return False


    def play_game(self):
        self.board = Board() # очистка поля
        while not self.play_round():
            pass # играем раунды пока не будет победителя или ничьи
        return True


    def start_games(self):
        while True:
            self.play_game()
            print(f"Счёт: {self.player1.name} - {self.player1.wins}, {self.player2.name} - {self.player2.wins}")
            if input("Хотите сыграть ещё раз? (да/нет): ").lower() != "да":
                break

# само использование
player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")
game = Game(player1, player2)
game.start_games()
